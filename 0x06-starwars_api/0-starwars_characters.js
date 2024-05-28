#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <film_id>');
  process.exit(1);
}

const id = process.argv[2];

const fetch_character = async (character) => {
  return new Promise((resolve, reject) => {
    request(character, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
};

request(`https://swapi-api.alx-tools.com/api/films/${id}/`, async function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      try {
        console.log(await fetch_character(character));
      } catch (error) {
        console.error('error:', error);
      }
    }
  }
});
