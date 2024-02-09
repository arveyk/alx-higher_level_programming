#!/usr/bin/node

const esrever = function (list) {
  const listRev = [];
  for (let len = list.length - 1; len >= 0; len--) {
    listRev.push(list[len]);
  }
  return (listRev);
};
exports.esrever = esrever;
