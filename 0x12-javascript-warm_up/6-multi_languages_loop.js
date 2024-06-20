#!/usr/bin/node
// script that prints 3 lines: (like 1-multi_languages.js) using array
const args = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
for (const arg in args) {
  console.log(args[arg]);
}
