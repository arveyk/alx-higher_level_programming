#!/usr/bin/node

exports.esrever = function (list) {
  const listRev = [];
  for (let len = list.length - 1; len >= 0; len--) {
    listRev.push(list[len]);
  }
  return (listRev);
};
