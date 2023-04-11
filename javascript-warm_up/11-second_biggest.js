#!/usr/bin/node
const args = process.argv.slice(2);
let secondBiggest = -Infinity;
let array = [];

if (args.length < 2) {
  secondBiggest = 0;
} else {
  array = args.sort((a, b) => b - a);
  secondBiggest = array[1];
}
console.log(secondBiggest);
