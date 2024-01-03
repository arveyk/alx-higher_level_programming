#!/usr/bin/node

request = require('request');
movieId = process.argv[2];
star_wrs = 'https://swapi-api.alx-tools.com/api/';

let characters = [];
request (star_wrs, function (error, response, body) {
  let bodyResp = JSON.parse(body);
    
    let url = bodyResp.people
    request (url, function (error, response, body) {
      let Resp = JSON.parse(body);
	/*console.log(Resp);*/

      for (count = 0; count < Resp.results.length; count++) {
	 characters.push(Resp.results[count].name);
      }
      for (nameCount = 0; nameCount < characters.length; nameCount++) {
	 console.log(characters[nameCount]);
      } 
    });
});

