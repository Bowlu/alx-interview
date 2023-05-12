#!/usr/bin/node

const request = require('request');

const movieURL = 'https://swapi-api.hbtn.io/api/films/';
if (process.argv.length > 2) {
  request(`${movieURL}/films/${process.argv[2]}/`, (err, res, body) => {
    if (err) {
      console.log(err);
    }
    const characterURL = JSON.parse(body).characters;
    const characterName = characterURL.map(url => new Promise((resolve, reject) => {
      request(url, (promiseErr, emp, characterBody) => {
        if (promiseErr) {
          reject(promiseErr);
        }
        resolve(JSON.parse(characterBody).name);
      });
    }));

    Promise.all(characterName)
      .then(cNames => console.log(cNames.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}