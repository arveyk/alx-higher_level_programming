#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

let count = 0
let num = 0
aUrl = 'https://swapi-alx.alx-tools.com/api/people/18/'
actorCount = 0;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const bodyResp = JSON.parse(body);
  for (count = 0; bodyResp.results; count++) {
    if (!(bodyResp.results[count])) {
      break;
    }
    for (num = 0; bodyResp.results[count].characters[num]; num++) {
	
	if (!(bodyResp.results[count].characters[num])) {
	   break;
	}
	if (bodyResp.results[count].characters[num] === aUrl) {
	   actorCount++;
	}
    }
  }
  console.log(actorCount);
});
