#!/usr/bin/node
// this script prints the first argument passed to it without using lenght
const argv = process.argv[2];
if (argv === undefined) {
  console.log('No argument');
} else {
  console.log(argv);
}
