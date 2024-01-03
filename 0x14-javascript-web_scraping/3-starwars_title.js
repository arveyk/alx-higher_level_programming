#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const bodyResp = JSON.parse(body);
  console.log(bodyResp.title);
});
