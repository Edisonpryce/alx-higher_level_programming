#!/usr/bin/node
//  script generates new array from an imported array
const arr = require('./100-data').list;
console.log(arr);
const newArr = list.map(function (num, index) {
  return num * index;
});
console.log(newArr);
