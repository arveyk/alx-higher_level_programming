#!/usr/bin/node
module.exports = function (x, theFunction) {
  while (x > 0) {
    theFunction();
    x += 1;
  }
};
