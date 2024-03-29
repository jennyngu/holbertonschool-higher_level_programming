#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || w === undefined) {
      return;
    }
    if (h <= 0 || h === undefined) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }

  rotate () {
    const newHeight = this.width;
    const newWidth = this.height;
    this.width = newWidth;
    this.height = newHeight;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
