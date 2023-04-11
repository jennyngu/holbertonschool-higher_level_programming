#!/usr/bin/node
let args = process.argv[2];

if (isNaN(args) === false || Number.isInteger(args) === true) {
  if (Number.isInteger(args) === false) {
    args = Math.floor(args);
  }
  for (let i = 0; i < args; i++) {
    for (let y = 0; y < args; y++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else if (Number.isInteger(args) === false || args[2] === null) {
  console.log('Missing size');
}
