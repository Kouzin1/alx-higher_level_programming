#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
    if (!error) {
        const characters = JSON.parse(body).charcters;
        printCharacters(characters, 0);
    }
});

function printCharacters (charcters, index) {
    request(characters[index], function (error, response, body) {
        if (!error) {
            console.log(JSON.parse(body).name);
            if (index + 1 < charcters.length) {
                printCharacters(charcters, index + 1);
            }
        }
    });
}
