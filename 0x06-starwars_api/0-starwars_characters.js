#!/usr/bin/node

const request = require('request');
const movie_id = process.argv[2];
const payload = { url: 'https://swapi-api.hbtn.io/api/films/' + movie_id, method: 'GET' };

request(payload, function (err, res, body) {
	if (!err) {
		const characters = JSON.parse(body).characters;
		Order(characters, 0);
	}
});

function Order (characters , n) {
	request(characters[n], function (err, res, body) {
		if (!err) {
			console.log(JSON.parse(body).name);
			if (n + 1 < characters.length) {
				Order(characters, n + 1);
			}
		}
	});
}
