const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/3/', function (error, response, body) {
  console.error('error:', error); // Print the error if one occurred
  console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
  JSON.parse(body).characters.forEach(character => {
    request(character, function (error, response, body) {
      console.log(JSON.parse(body).name);
    });
  });
});
