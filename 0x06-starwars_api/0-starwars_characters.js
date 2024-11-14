#!/usr/bin/env node

const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Construct the URL for the specific movie
const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make a request to the Star Wars API
request(filmUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to retrieve data:', response.statusCode);
    return;
  }

  // Parse the response body
  const movieData = JSON.parse(body);

  // Iterate over each character URL and fetch the character name
  movieData.characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      if (response.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      } else {
        console.error('Failed to retrieve character data:', response.statusCode);
      }
    });
  });
});
