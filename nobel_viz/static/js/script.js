// static/js/script.js 
var API_URL = 'http://localhost:5000/api';  

var displayJSON = function(query) {   
	$('#query pre').html(query); 
//	d3.select('#data pre').html(JSON.stringify(data, null, 4));  
	console.log(data);  
	}); 
};  

var query = '/winners_cleaned?where=' + JSON.stringify(
	{ "year":{"$gt":2000},  
	  "gender": "female" }
	);  
//var query = "/winners_cleaned\?where='{"country":"Russia"}' "
console.log(query);
displayJSON(query);
