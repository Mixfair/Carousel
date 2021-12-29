const axios = require('axios');
const agent = require('./agent');

const serverUrl = 'https://localhost:4433/api/get/cookie';
let opts = { httpsAgent: agent('alice') };

axios.post(serverUrl, opts)
	.then((res) => {
		console.log(res.data);
	})
	.catch((err) => {
		console.error(err);
	});
