#!/usr/bin/node
const args = process.argv;

if (args[2] != null && args[3] != null) {
  console.log(args[2] + ' is ' + args[3]);
} else if (args[2] != null && args[3] == null) {
  console.log(args[2] + ' is undefined');
} else if (args[2] == null && args[3] != null) {
  console.log('undefined is ' + args[3]);
} else {
  console.log('undefined is undefined');
}
