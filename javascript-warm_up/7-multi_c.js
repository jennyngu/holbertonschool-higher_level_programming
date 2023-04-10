#!/usr/bin/node
let args = process.argv[2];

if (isNaN(args) === false || Number.isInteger(args) === true) {
  if (Number.isInteger(args) === false) {
    args = Math.floor(args);
  }
  for (let i = 0; i < args; i++) {
    console.log('C is fun');
  }
} else if (Number.isInteger(args) === false || args[2] === null) {
  console.log('Missing number of occurrences');
}
