#!/usr/bin/node

const request = require('request');
/* const movieId = process.argv[2]; */
const starWrs = 'https://swapi-api.alx-tools.com/api/';

const characters = [];

request(starWrs, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const bodyResp = JSON.parse(body);

  const url = bodyResp.people;
  request(url, function (error, response, body) {
    if (error) {
      console.error(error);
    }
    const Resp = JSON.parse(body);
    /* console.log(Resp); */

    for (let count = 0; count < Resp.results.length; count++) {
      characters.push(Resp.results[count].name);
    }
    /*
     * for (let nameCount = 0; nameCount < characters.length; nameCount++) {
      console.log(characters[nameCount]);
    }
    */
  });
});

if (characters) {
  process.stdout.write('OK');
}
