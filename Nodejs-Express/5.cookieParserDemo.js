var express = require('express');
var app = express();


var bodyParser = require('body-parser');
var cookieParser = require('cookie-parser');

app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies
app.use(cookieParser());

app.get('/', function(request, response){
    response.sendFile(__dirname + "/cookiePOST.html");
})

app.post('/cookie',function(request, response){
  //get first name from request.body
  var fname = request.body.first_name;
  //set cookie - res.cookie('cookieName', 'cookieValue')
  response.cookie("name", username);
  response.send("cookie set");
})


var server = app.listen(8080, 'localhost', function(){   //'localhost' specifies to listen only to localhost
	var host = server.address().address;
	var port = server.address().port;

	console.log("Example app listening at http://%s:%s", host, port);
})
