#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(body);
});

const bodyResp = JSON.parse(body)
tasks = {'1': 0,
	 '2': 0,
	 '3': 0,
	 '4': 0,
	 '5': 0,
	 '6': 0,
	 '7': 0,
	 '8': 0,
	 '9': 0,
	 '10': 0
}

for (let count = 0; count < tasks.length) {
  if (tasks[count] == bodyResp[count]) {
    for (bodyResp[count]) {
      if (bodyResp[count].completed === 'true'
        tasks[]
    }
  }
}
