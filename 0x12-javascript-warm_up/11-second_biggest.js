#!/usr/bin/node
// this task searches the second biggest integer in the list of arguments
const myList = process.argv;
if (myList.length <= 3) {
  console.log(0);
} else {
  console.log(myList.sort((x, y) => y - x).slice(3)[0]);
}
