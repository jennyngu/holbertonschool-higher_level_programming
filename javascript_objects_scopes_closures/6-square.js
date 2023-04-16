#!/usr/bin/node
const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        for (let y = 0; y < this.width; y++) {
          process.stdout.write(c);
        }
        console.log('');
      }
    } else {
      super.print();
    }
  }
};
