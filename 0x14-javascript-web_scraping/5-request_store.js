#!/usr/bin/node
/**
 * Utilizing requests and fs modules to send get request to a URL
 * and also using the fs module for file io.
 */
const request = require('request');
const fs = require('fs');
request.get(process.argv[2], (err, response, body) => {
  if (err) {
    console.error('Error: ', err);
    return;
  }
  fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
    if (err) {
      console.error('Error: ', err);
    }
  });
});
