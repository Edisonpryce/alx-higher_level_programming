#!/usr/bin/node
/**
 * Utilizing the fs module
 * WriteFile method from the fs module was used
 * to write a string to a file.
 */
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) {
    console.error('Error: ', err);
  }
});
