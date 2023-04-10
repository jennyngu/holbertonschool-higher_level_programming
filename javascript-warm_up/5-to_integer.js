#!/usr/bin/node
let args = process.argv[2];

if (isNaN(args) === false || Number.isInteger(args) === true) {
  if (Number.isInteger(args) === false) {
    args = Math.floor(args);
  }
  console.log('My number: ' + args);
} else if (Number.isInteger(args) === false) {
  console.log('Not a number');
}
