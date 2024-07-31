#!/usr/bin/node
/**
 * Request method to make a GET request to the Star Wars
 * API to get all the characters of Star Wars Movie
 */
const request = require('request');
const url = process.argv[2];
const myDict = {};

request(url, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    const response = JSON.parse(body);

    for (let i = 0; i < response.length; i++) {
      if (response[i].completed === true) {
        if (myDict[response[i].userId] === undefined) {
          myDict[response[i].userId] = 1;
        } else {
          myDict[response[i].userId] += 1;
        }
      }
    }
  }
  console.log(myDict);
});
