#!/usr/bin/node
// prints number of arguments printed and the new argument value 
let i = 0;
exports.logMe = function (item) {
  console.log(i + ': ' + item);
  i++;
};
