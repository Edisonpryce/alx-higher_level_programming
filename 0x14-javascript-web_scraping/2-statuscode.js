#!/usr/bin/node
/**
 * Utilizing the request module.
 * Request module makes a GET request to specified URL.
 */
let statusC;
const request = require('request');
request.get(process.argv[2], (err, response, body) => {
  if (err) {
    console.error('Error: ', err);
    return;
  }
  statusC = response.statusCode;
  console.log('code: ', statusC);
});
