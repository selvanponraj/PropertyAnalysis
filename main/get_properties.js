const realtor = require('realtorca');
const fs = require('fs');

let opts = {
	LongitudeMin: -82.9758985519409,
	LongitudeMax: -75.347015,
	LatitudeMin: 40.07601549736786,
	LatitudeMax: 45.651070,
	PriceMin: 0,
	PriceMax: 1000000000,
	TransactionTypeId:2 ## for sale
	MaximumResults: 100000000
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