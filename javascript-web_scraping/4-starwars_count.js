#!/usr/bin/node

const request = require('request');
const charId = 'https://swapi-api.hbtn.io/api/people/18/';
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).results;
  const count = films.filter((film) =>
    film.characters.includes(charId)
  ).length;

  console.log(count);
});
