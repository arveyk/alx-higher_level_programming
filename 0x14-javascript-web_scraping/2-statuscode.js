#!/usr/bin/node

const url = process.argv[2];
const fetch = (...args) => import ('node-fetch').then(({default: fetch}) => fetch(...args)); 
const request = require('require')

request(url, function (error, response, body) {
  console.error('error', error);
  console.log('statusCode:', response.statusCode);
});

/*
fetch(url)
	.then((response) => response.text())
	.then((data) => {
	    console.log(data);
	})
	.catch((error) => {
	    console.error(error);
	});
	*/

/*
 * const response = fetch(url);
console.log(response.status);
*/
