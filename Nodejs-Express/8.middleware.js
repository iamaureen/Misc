//https://expressjs.com/en/guide/writing-middleware.html
var express = require('express');
var app = express();

//middleware:1
// This function just prints “LOGGED” when a request to the app passes through it.
// The middleware function is assigned to a variable named myLogger.
var myLogger = function (req, res, next) {
  console.log('LOGGED');
  next();  //if this next is not given, the app will not complete the request-response cycle, hence the browser will hang
            //goes to middleware:2
};
//middleware:2
var requestTime = function (req, res, next) {
  req.requestTime = Date.now();
  next(); //if this next is not given, the app will not complete the request-response cycle, hence the browser will hang
          // goes to app.get('/')
};

//to load the middleware, call app.use() specifying middleware function.
app.use(myLogger);
app.use(requestTime);

app.get('/', function (req, res) {
  var responseText = 'Hello World!<br>';
  responseText += 'Requested at: ' + req.requestTime + '';
  res.send(responseText);
});

//Every time the app receives a request, it prints the message “LOGGED” to the terminal.
//The order of middleware loading is important: middleware functions that are loaded first are also executed first.
//If myLogger is loaded after the route to the root path, the request never reaches it and the app doesn’t
//print “LOGGED”, because the route handler of the root path terminates the request-response cycle.
//The middleware function myLogger simply prints a message, then passes on the request to the next middleware
//function in the stack by calling the next() function.


app.listen(8080);
