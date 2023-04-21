#!/usr/bin/node

const request = require('request');
const searchWA = 'https://swapi-api.hbtn.io/api/people/18/';
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) console.log(error);
  const bodyInfo = JSON.parse(body);
  const results = bodyInfo.results;
  let count = 0;
  for (let i = 0; i < results.length; i++) {
    const characters = results[i].characters;
    if (characters.includes(searchWA)) {
      count = count + 1;
    }
  }
  console.log(count);
});
