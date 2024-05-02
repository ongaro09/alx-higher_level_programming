#!/usr/bin/node

const axios = require('axios');

async function getCharactersByMovieId(movieId) {
    try {

        const response = await axios.get(
	    `https://swapi.dev/api/films/${movieId}/`
	);


        const characterUrls = response.data.characters;


        const characterPromises = characterUrls.map(url => axios.get(url));
        const charactersResponses = await Promise.all(characterPromises);


        charactersResponses.forEach(characterResponse => {
            console.log(characterResponse.data.name);
        });
    } catch (error) {
        console.error('Failed to fetch data:', error);
    }
}

