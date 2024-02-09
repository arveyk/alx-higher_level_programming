#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, function (err, data) {
  if (err) {
    throw err;
  }
  fs.writeFile(fileC, data, { flag: 'a+' }, (err) => {
    if (err) {
      throw err;
    }
  });
});

fs.readFile(fileB, function (err, data) {
  if (err) {
    throw err;
  }
  fs.writeFile(fileC, data, { flag: 'a+' }, (err) => {
    if (err) {
      throw err;
    }
  });
});
