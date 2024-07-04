#!/usr/bin/node
// convertion of a number from base 10 to base passed to it as an argument */
exports.converter = function (base) {
  return function (argv) {
    return argv.toString(base);
  };
};
