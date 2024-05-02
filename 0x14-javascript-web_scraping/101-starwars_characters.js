#!/usr/bin/node
const request = require('request');

function getCharactersByMovieId(movieId) {
    console.log("Starting fetch for movie ID:", movieId);
    request(`https://swapi-api.alx-tools.com/films/${movieId}`, { json: true }, (err, res, body) => {
        if (err) { return console.log(err); }
        console.log("Movie data fetched:", body);

        const characterUrls = body.characters;
        console.log("Character URLs:", characterUrls);

        let completedRequests = 0;
        const characters = [];

        characterUrls.forEach(url => {
            request(url, { json: true }, (err, res, body) => {
                if (err) { return console.log(err); }
                characters.push(body.name);
                completedRequests++;
                if (completedRequests === characterUrls.length) {

                    console.log("Characters fetched:");
                    characters.forEach(name => {
                        console.log(name);
                    });
                }
            });
        });
    });
}

