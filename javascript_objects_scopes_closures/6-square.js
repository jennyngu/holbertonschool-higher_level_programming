#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        for (let y = 0; y < this.width; y++) {
          process.stdout.write('C');
        }
        console.log('');
      }
    } else {
      super.print();
    }
  }
};
