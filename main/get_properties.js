const realtor = require('realtorca');
const fs = require('fs');

let opts = {
	LongitudeMin: -79.6758985519409,
	LongitudeMax: -79.6079635620117,
	LatitudeMin: 43.57601549736786,
	LatitudeMax: 43.602250137362276,
	PriceMin: 100000,
	PriceMax: 410000
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