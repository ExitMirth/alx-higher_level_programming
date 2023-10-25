#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    const characters = film.characters;

    function fetchCharacter (index) {
      if (index < characters.length) {
        request(characters[index], (err, charResponse, charBody) => {
          if (!err && charResponse.statusCode === 200) {
            const character = JSON.parse(charBody);
            console.log(character.name);
            fetchCharacter(index + 1);
          } else {
            console.log('Error fetching character data');
          }
        });
      }
    }

    fetchCharacter(0);
  } else {
    console.log('Error fetching film data');
  }
});
