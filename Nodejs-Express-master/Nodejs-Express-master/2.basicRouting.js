//Routing refers to determining how an application responds to a client request to a particular endpoint,
//which is a URI (or path) and a specific HTTP request method (GET, POST, and so on).

//https://www.tutorialspoint.com/nodejs/nodejs_express_framework.htm

var express = require('express');
var app = express();

//Express provides a built-in middleware express.static to serve static files,
//such as images, CSS, JavaScript, etc.
//You simply need to pass the name of the directory where you keep your static assets,
//to the express.static middleware to start serving the files directly.

app.use(express.static(__dirname));   //curent directory-->__dirname
//access with: http://localhost:8080/flower1.jpg, http://localhost:8080/images/flower1.jpg

app.get('/', function(request, response){
	console.log("Got a GET request for the homepage")
	response.send('Hello GET');
})

var server = app.listen(8080, function(){
	var host = server.address().address;
	var port = server.address().port;

	console.log("Example app listening at http://%s:%s", host, port);
})
