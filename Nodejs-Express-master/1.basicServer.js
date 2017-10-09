//Following is a very basic Express app which starts a server and listens on port 3000 for connection.
//This app responds with Hello World! for requests to the homepage. For every other path,
//it will respond with a 404 Not Found.

//https://www.tutorialspoint.com/nodejs/nodejs_express_framework.htm


var express = require('express');
var app = express();

app.get('/', function(request, response){

	setTimeout(function(str1, str2) {
  	console.log(str1 + " " + str2);
		response.send('Hello World');
	}, 10000, "Hello.", "How are you?");


})

var server = app.listen(8080, function(){
	var host = server.address().address;
	var port = server.address().port;

	console.log("Example app listening at http://%s:%s", host, port);
})
