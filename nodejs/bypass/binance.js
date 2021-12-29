const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
const AdblockerPlugin = require('puppeteer-extra-plugin-adblocker');
puppeteer.use(StealthPlugin());
puppeteer.use(AdblockerPlugin({ blockTrackers: true }));
const fs = require('fs');
const delay = require('delay');
const { getCode }  = require('./imap.js');
const exec = require('child_process').exec;
const OTPAuth = require('otpauth');

const path = require('path');
const { Console } = require('console');
const moduleDir = path.resolve(__dirname);
const rootDir = path.dirname(require.main.filename);

module.exports = {

    fetchCreds: async (email, password, imapToken, oauthUri) => {

      const options = {waitUntil: 'networkidle2'}
      const browser = await puppeteer.launch({ headless: true,args: [
      '--remote-debugging-port=9222',
      "--remote-debugging-address=0.0.0.0",
      '--no-sandbox', '--disable-setuid-sandbox',
      '--disable-gpu', "--disable-features=IsolateOrigins,site-per-process", '--blink-settings=imagesEnabled=true'
      ]});

      const page = await browser.newPage();
      console.log(`Proccessing email: ${email}`)

      await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36');
      await page.goto(`https://accounts.binance.com/en/login`, options)

      await bypassSlider(page, email, password)

      console.log('Login Done! Going to ' + page.url())

      let result = await verifyProccess(page, email, imapToken, oauthUri)

      console.log("2FA Bypassed!")

      await page.close();
      await browser.close()

      return result
    }
}


async function verifyProccess(page, email, imapToken, oauthUri) {

  var headers

  await page.waitForSelector('.css-1mme6xj')
  await page.click('.css-1mme6xj')

  await delay(10000)

  let authCode = await getCode(email, imapToken)

  const verifyCode = await page.waitForSelector('.css-16fg16t[aria-label="E-mail verification code"]')
  await verifyCode.type(authCode)

  await page.screenshot({path: `${moduleDir}/tmp/entered.png`});

  console.log(`Received mail code: ${authCode}`)

  let confirmToken = await getOtpAuth(oauthUri)

  console.log(`Received otp code: ${confirmToken}`)

  const verifyToken = await page.waitForSelector('.css-16fg16t[aria-label="Authenticator Code"]')
  await verifyToken.type(confirmToken)

  const confirmCode = await page.waitForSelector('.css-1jauszb')
  await confirmCode.click()

  await delay(5000)
  const authedPage = await page.waitForSelector('.css-wu6zme')

  page.on('response', async response => {
    if (response.request().url().includes('public/authcenter/auth')) {
      headers = response.request().headers()
    }
  })

  await page.goto('https://www.binance.com/en/nft');
  await page.evaluate( function(){

    siteKey = JSON.parse(document.getElementById('__APP_DATA').textContent).runtimeConfig.GOOGLE_KEY

    grecaptcha.ready(function() {
      grecaptcha.execute(siteKey).then(function(token) {
        document.cookie = `x-nft-checkbot-sitekey=${siteKey}`;
        document.cookie = `x-nft-checkbot-token=${token}`;
      });
    });

  } );

  await delay(3000)
  let cookies = await page.cookies()
  console.log(await page._client.send('Network.getAllCookies'))
  // console.log(cookies)

  headers['x-nft-checkbot-sitekey'] = cookies.find(cookie => cookie.name == 'x-nft-checkbot-sitekey').value
  headers['x-nft-checkbot-token'] = cookies.find(cookie => cookie.name == 'x-nft-checkbot-token').value

  cookies = cookies.filter(cookie => cookie.name !== 'x-nft-checkbot-sitekey' && cookie.name !== 'x-nft-checkbot-token' )

  let cookieHeader = cookies.map((cookie) => { return `${cookie.name}=${cookie.value};` }).join(' ')

  headers['cookie'] = cookieHeader

  // console.log(headers)
  // console.log(cookies)

  return headers
}

async function getOtpAuth(uri) {

  let parsedTotp = OTPAuth.URI.parse(uri);

  var authToken = parsedTotp.generate()

  return authToken
}

async function submitUserData(page, email, password) {
  const emailField = await page.waitForSelector('input[name=email]')
  await emailField.click({ clickCount: 3 })
  await emailField.type(email)

  const passwordField = await page.waitForSelector('input[name=password]')
  await passwordField.click({ clickCount: 3 })
  await passwordField.type(password)

  const captchaCall = await page.waitForSelector('#click_login_submit')
  await captchaCall.click()

  console.log('Data entered...')
}

async function bypassSlider(page, email, password) {

  await page.removeAllListeners("request");

  await submitUserData(page, email, password)
  await moveSlider(page)

  try {
    // await page.screenshot({path: `${rootDir}/tmp/afterapplied.png`});
    await page.waitForSelector('.css-key3v2', { visibe: true, timeout: 15000 });
  } catch (e) {
    try {
      console.log('Failed! Trying to close slider frame..')
      await page.screenshot({path: `${rootDir}/tmp/afterappliedfail1.png`});
      await page.waitForSelector('svg[cursor=pointer]', { timeout: 2000 })
      await page.click('svg[cursor=pointer]')
    } catch(e) {
      await page.screenshot({path: `${rootDir}/tmp/afterappliedfail2.png`});
      console.log('Apllying scroll failed!')
    }
    // await page.screenshot({path: 'buddy-screenshot2.png'});
    await delay(2000)

    return bypassSlider(page, email, password)
  }
}

async function moveSlider(page) {
  let originalImage = ''

  await page.setRequestInterception(true);

  page.on('request', request => request.continue())

  page.on('response', async response => {
      if (response.request().url().includes('image/antibot/image/SLIDE/')) {
          originalImage = await response.buffer().catch(() => {});
      }
      // if (response.status() != 200 ) {
      //   console.log(await response.text())
      // }
  })

  const sliderButton = '.css-13rz4tr'
  const handlerButton = ".css-p72bjc"
  try {
    await page.waitForSelector(".css-13rz4tr", { visibe: true, timeout: 10000 });
  } catch (e) {
    await page.screenshot({path: `${moduleDir}/tmp/whenloadingslider.png`});
    throw(e)
  }

  const sliderElement = await page.$('.css-13rz4tr');
  const slider = await sliderElement.boundingBox();

  await page.waitForSelector(handlerButton, { visibe: true, timeout: 5000 });
  const sliderHandler = await page.$(handlerButton);
  const handler = await sliderHandler.boundingBox();


  await fs.writeFileSync(`${moduleDir}/tmp/fetched.png`, originalImage, 'binary');

  console.log('Picture fetched!')

  exec(`compare -metric RMSE -subimage-search ${moduleDir}/tmp/fetched.png ${moduleDir}/etalon.png ${moduleDir}/tmp/fetched.png`,
    async (error, stdout, stderr) => {
      const x = error.toString().split('@')[error.toString().split('@').length-1].trim().split(',')[0];
      const y = error.toString().split('@')[error.toString().split('@').length-1].trim().split(',')[1];

      console.log('Start moving..')
      await delay(200)

      await page.mouse.move(handler.x, handler.y);
      await page.mouse.down();
      const valueData = (parseInt(x)-64) //64
      let currentPosition = 0

      for (let index = 0; index < valueData; index++) {
          await page.mouse.move(handler.x+currentPosition, handler.y);
          currentPosition = index++
      }
      await page.mouse.move(handler.x+currentPosition, handler.y, {stpes:10});
      // await delay(500)
      await page.mouse.up();

      await page.screenshot({path: `${moduleDir}/tmp/applied.png`});
   });
}
