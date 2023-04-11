#!/usr/bin/node
const arg = process.argv[2];

function factorial (arg) {
  if (arg === undefined) {
    return (1);
  } else if (arg === 0 || arg === 1) {
    return (1);
  } else {
    return (arg * factorial(arg - 1));
  }
}
console.log(factorial(arg));
