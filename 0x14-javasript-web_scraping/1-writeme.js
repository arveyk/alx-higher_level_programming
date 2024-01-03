#!/usr/bin/node

const fs = require('fs');

fileName = process.argv[2];
text = process.argv[3];

fs.writeFile(fileName, text, err => {
  if (err) {
    console.error(error);
  }
});

