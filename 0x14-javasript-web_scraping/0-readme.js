#!/usr/bin/node

const fs = require('fs');
file = process.argv[2]

fs.readFile(file, (err, data) => {
  if (err) throw err;
  console.log(data.toString());
});
