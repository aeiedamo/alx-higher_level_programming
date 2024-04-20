#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w < 1 || h < 1) return;
    this.width = w;
    this.height = h;
  }

  print () {
    const ch = 'X';
    for (let i = 0; i < this.height; i++) console.log(ch.repeat(this.width));
  }

  rotate () {
    const save = this.width;
    this.width = this.height;
    this.height = save;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
