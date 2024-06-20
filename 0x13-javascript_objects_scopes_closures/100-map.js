#!/usr/bin/node
//  script generates new array from an imported array
const array = require('./100-data').list;
console.log(array);
console.log(array.map(function (x, i) { return (x * i); }));
