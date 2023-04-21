#!/usr/bin/node

const request = require('request');
const searchWA = '/18/';
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) console.log(error);
  const bodyInfo = JSON.parse(body);
  const results = bodyInfo.results;
  let count = 0;
  for (const i in results) {
    const characters = results[i].characters;
    for (const char in characters) {
      if (characters[char].includes(searchWA)) {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
