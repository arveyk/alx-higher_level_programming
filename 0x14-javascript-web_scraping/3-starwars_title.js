#!/usr/bin/node
const url = process.argv[2];
const fetch = (...args) => import ('node-fetch').then(({default: fetch}) => fetch(...args)); 

/* request(url, function (error, response, body) {
  console.error('error', error);
  console.log('statusCode:', response && response.statusCode);
});
*/

fetch(url)
	.then((response) => response.text())
	.then((data) => {
	    console.log(data);
	})
	.catch((error) => {
	    console.error(error);
	});
