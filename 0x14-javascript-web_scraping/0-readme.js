#!/usr/bin/node
/**
 * Utilizing the fs module for file functionalities.
 * The readFile method was used to read a file.
 */
const fs = require('fs');
filepath = process.argv[2];
fs.readFile(filepath, 'utf-8', (err, data) => {
  if (err) {
    console.error('Error: ', err);
    return;
  }
  console.log(data);
});
