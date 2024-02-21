#!/usr/bin/node
/* Write a script that prints all characters of a Star Wars movie:
    - The first argument is the movie ID
    - You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
    - You must use the module request
*/
const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <film_id>');
  process.exit(1);
}

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;

    for (let i = 0; i < characters.length; i++) {
      request(character[i], function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
