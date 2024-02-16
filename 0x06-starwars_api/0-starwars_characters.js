#!/usr/bin/node
/* Write a script that prints all characters of a Star Wars movie:
    - The first argument is the movie ID
    - You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
    - You must use the module request
*/


const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
})

