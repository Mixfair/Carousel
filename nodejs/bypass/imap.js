var imaps = require('imap-simple');
const _ = require('lodash');
const simpleParser = require('mailparser').simpleParser

module.exports = {
    getCode: async (email, pwd) =>
    {
        var result = ''
        let config = {
            imap: {
                user: email,
                password: pwd,
                host: 'imap.mail.ru',
                port: 993,
                tls: true,
                authTimeout: 3000
            }
        };

        let connection =  await imaps.connect(config)

        await connection.openBox('INBOX')

        let delay = 24 * 3600 * 1000;
        let yesterday = new Date();
        yesterday.setTime(Date.now() - delay);
        yesterday = yesterday.toISOString();

        let searchCriteria = [['UNSEEN'], ['SINCE', yesterday]];
        let fetchOptions = { bodies: ['HEADER', ''], markSeen: true};

        let messages = await connection.search(searchCriteria, fetchOptions);

        messages.forEach(async function (item) {

            const fullBody = _.find(item.parts, {which: ''})

             simpleParser(fullBody.body, (err, mail) => {
                if (mail.subject.includes('[Binance]Authorize New')){
                    const otp = mail.html.match(/(class="bigVertifyCode".*>)(\d*)(<\/div>)/);
                    result = otp[2]
                }
            });
        });

        await new Promise((resolve, reject) => setTimeout(resolve, 5000));

        connection.end()
        return result
    }
}
