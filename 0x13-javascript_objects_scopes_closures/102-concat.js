#!/usr/bin/node
// concatenation of 2 files
const fl = require('fs');
const File1 = fl.readFileSync(process.argv[2]).toString();
const finalFile = fl.readFileSync(process.argv[3]).toString();
fl.writeFileSync(process.argv[4], (firstFile + secondFile));
