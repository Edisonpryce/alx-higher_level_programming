#!/usr/bin/node
/**
 * Request module make a GET request to the Star Wars
 * API which returns with the list of films.
 */
const request = require('request');
let bodyResponse;
request.get(process.argv[2], (err, response, body) => {
  if (err) {
    console.error('Error: ', err);
    return;
  }
  bodyResponse = JSON.parse(body);
  let counter = 0;
  for (let i = 0; i < bodyResponse.results.length; i++) {
    if (bodyResponse.results[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      counter += 1;
    }
  }
  console.log(counter);
});
