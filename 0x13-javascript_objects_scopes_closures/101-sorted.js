#!/usr/bin/node
/* This script imports dictionary of occurrences by the user id and computes a dictionary of user ids by occurrence */
const dic = require('./101-data').dict;
const newDic = {};
Object.keys(dic).map(function (key, index) {
  if (newDic[dic[key]] === undefined) {
    newDic[dic[key]] = [];
  }
  newDic[dic[key]].push(key);
});

console.log(newDic);
