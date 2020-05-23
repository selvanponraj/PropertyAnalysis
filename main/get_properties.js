const realtor = require('realtorca');
const fs = require('fs');

// Set default values
var minLong = -79.6758985519409;
var maxLong = -79.6079635620117;
var minLat = 43.57601549736786;
var maxLat = 43.602250137362276;
var minPrice = 100000;
var maxPrice = 410000;

var argv = require('minimist')(process.argv.slice(2));
console.dir(argv);

// Override default values with arguments if they exit
if (typeof argv['minLong'] != 'undefined') {
    minLong = Number(argv['minLong']);
}
if (typeof argv['maxLong'] != 'undefined') {
    maxLong = Number(argv['maxLong']);
}
if (typeof argv['minLat'] != 'undefined') {
    minLat = Number(argv['minLat']);
}
if (typeof argv['maxLat'] != 'undefined') {
    maxLat = Number(argv['maxLat']);
}
if (typeof argv['minPrice'] != 'undefined') {
    minPrice = Number(argv['minPrice']);
}
if (typeof argv['maxPrice'] != 'undefined') {
    maxPrice = Number(argv['maxPrice']);
}

let opts = {
	LongitudeMin: minLong,
	LongitudeMax: maxLong,
	LatitudeMin: minLat,
	LatitudeMax: maxLat,
	PriceMin: minPrice,
	PriceMax: maxPrice
};

realtor.post(opts)
	.then(data => {
		// console.log(data)
		var writer = fs.createWriteStream('output.json');
		var json = JSON.stringify(data)
		writer.write(JSON.stringify(data, null, 2));
	})
	.catch(err => {
		
});