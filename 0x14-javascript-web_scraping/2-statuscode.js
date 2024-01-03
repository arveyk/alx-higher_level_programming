#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log('code:', response && response.statusCode);
});
