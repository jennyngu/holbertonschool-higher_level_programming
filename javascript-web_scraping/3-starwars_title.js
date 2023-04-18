#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);

  const bodyInfo = JSON.parse(body);
  const movieTitle = bodyInfo.title;
  console.log(movieTitle);
});
