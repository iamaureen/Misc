var express = require('express');
var app = express();

//Route parameters are named URL segments that are used to capture the values specified at their position
//in the URL. The captured values are populated in the req.params object, with the name of the route parameter
// specified in the path as their respective keys.
//
// try: http://localhost:8080/users/34/books/8989 in the browser
app.get('/users/:userId/books/:bookId', function(request, response){

  //get the values individually from request.params
  var value = {
    uid: request.params.userId,
    bid: request.params.bookId
  }
  console.log("value::"+JSON.stringify(value));

  response.send(request.params);
})

app.listen(8080);
