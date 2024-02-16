#!/usr/bin/node


const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/people/';

request(url, function (error, response, body) {
    if (error) {
        console.error('error:', error);
    } else {
        const results = JSON.parse(body).results;
        for (let i = 0; i < results.length; i++) {
        console.log(results[i].name);
        }
    }
});
