const express = require('express');
const fs = require('fs');
const https = require('https');
const path = require('path');
const YAML = require('yaml');

const rootDir = path.dirname(require.main.filename);

const opts = {
	key: fs.readFileSync(path.join(__dirname, 'security/server-key.pem')),
	cert: fs.readFileSync(path.join(__dirname, 'security/server-cert.pem')),
	requestCert: true,
	rejectUnauthorized: true,
	ca: [fs.readFileSync(path.join(__dirname, 'security/ca-chain.pem'))]
};

queue = []

var configData = fs.readFileSync(path.join(__dirname, 'config.yml'), 'utf8')

var configMap = YAML.parse(configData)

const app = express();

app.get('/', (req, res) => {
	res.send('<a href="/authenticate">Log in using client certificate</a>');
});

app.post('/api/get/carousel', (req, res) => {
	const cert = req.socket.getPeerCertificate();

	console.log(req.client.authorized)
	try {
		let config = configMap.pop()
		let msg = {
			headers: queue.pop().headers,
			settings: config
		}

		// console.log(msg)

		res.status(200)
	  	.json(msg)

		var ip = req.headers['x-forwarded-for'] || req.socket.remoteAddress
		console.log(`[${ip}] given task: ${JSON.stringify(config)}`)
	} catch(e) {
		res.status(500)
			.send('Queue is empty.')
		console.log("Last taked!")
	}
})

app.get('/api/get/success', (req, res) => {
	res.status(200)
		.send("OK")
	console.log("Succes buying")
})

https.createServer(opts, app).listen(4433, () => {

	var nodesPerCred = 2
	var storage = YAML.parse(fs.readFileSync(`${rootDir}/../out/storage.yml`, 'utf-8'))

	let headersFetched = storage.map( cred => cred )
	queue = Array.from({length: nodesPerCred}, () => headersFetched).flat()

	const msg = `Carousel started at PORT:4433 Queue: ${queue.map(it => it.cred.email)}`
	console.log(msg)
});
