const { fetchCreds } = require('./binance.js')
const fs = require('fs')
const path = require('path')
const YAML = require('yaml')

const rootDir = path.dirname(require.main.filename);
const outPath = `${rootDir}/../out/storage.yml`

var creds = YAML.parse(fs.readFileSync(`${rootDir}/creds.yml`, 'utf-8'))

if (process.argv[2] == 'clean') {
  fs.writeFileSync(outPath, '');
}

(async () => {

  for(let credential of creds) {

    let email = credential.email
    let password = credential.password
    let imapToken = credential.imapToken
    let oauth = credential.oauth

    console.log('Start ' + email)

    let headers = await fetchCreds(email, password, imapToken, oauth)

    let fetchedData = [{
      cred: credential,
      headers: headers
    }]

    fs.appendFileSync(outPath, YAML.stringify(fetchedData));
  }

})()
