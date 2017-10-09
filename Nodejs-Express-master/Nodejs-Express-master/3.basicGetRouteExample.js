//this example passes two values using HTML FORM GET method.
// We are going to use process_get router inside server.js to handle this input.

//https://www.tutorialspoint.com/nodejs/nodejs_express_framework.htm

var express = require('express');
var app = express();

//Express provides a built-in middleware express.static to serve static files,
//such as images, CSS, JavaScript, etc.
//You simply need to pass the name of the directory where you keep your static assets,
//to the express.static middleware to start serving the files directly.

app.use(express.static(__dirname));
//access with: http://localhost:8080/flower1.jpg, http://localhost:8080/images/flower1.jpg
//


//access: http://localhost:8080/indexGet.html
app.get('/indexGet.html', function(request, response){
	console.log("I am here::" + __dirname);
	response.sendFile(__dirname + "/indexGet.html");
})

app.get('/process_get', function(request, response){
	//prepare output in json format
	var res={
		fname: request.query.first_name,
		lname: request.query.last_name
	}

	console.log("response from html::"+res);

	response.end(JSON.stringify(res));
})


var server = app.listen(8080, 'localhost', function(){   //'localhost' specifies to listen only to localhost
	var host = server.address().address;
	var port = server.address().port;

	console.log("Example app listening at http://%s:%s", host, port);
})
