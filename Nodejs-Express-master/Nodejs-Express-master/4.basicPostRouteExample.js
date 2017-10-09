//this example passes two values using HTML FORM POST method.
// We are going to use process_get router inside server.js to handle this input.
// To get POST parameters, we’ll need two the ExpressJS body-parser package.
// This will allow us to grab information from the POST.

//https://scotch.io/tutorials/use-expressjs-to-get-url-and-post-parameters

var express = require('express');
var app = express();

var bodyParser = require('body-parser');

//Express provides a built-in middleware express.static to serve static files,
//such as images, CSS, JavaScript, etc.
//You simply need to pass the name of the directory where you keep your static assets,
//to the express.static middleware to start serving the files directly.

app.use(express.static(__dirname));
//access with: http://localhost:8080/flower1.jpg, http://localhost:8080/images/flower1.jpg
app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies


//access: http://localhost:8080/indexGet.html
app.get('/indexGet.html', function(request, response){
	console.log("I am here::" + __dirname);
	response.sendFile(__dirname + "/indexGet.html");
})

app.post('/process_get', function(request, response){
	//We will grab POST parameters using req.body.variable_name
	var fname = request.body.first_name;
	var lname = request.body.last_name;
	//prepare output in json format
	var res={
		fname: fname,
		lname: lname
	}

	console.log("response from html::"+JSON.stringify(res));

	response.end(JSON.stringify(res));
})


var server = app.listen(8080, 'localhost', function(){   //'localhost' specifies to listen only to localhost
	var host = server.address().address;
	var port = server.address().port;

	console.log("Example app listening at http://%s:%s", host, port);
})
