//https://scotch.io/tutorials/use-ejs-to-template-your-node-application

var express = require('express');
var app = express();

//set the view engine to ejs
app.set('view engine', 'ejs');

//res.render - used to load up ejs view file
app.get('/', function(request, response){
  response.render('index.ejs');
})

app.get('/about', function(request, response){
  //it looks into views/about.ejs automatically
  //so no need to write views/about.ejs
  response.render('about.ejs');

})

//passing values to views
//single variable and array of variables
app.get('/passInfo', function(request, response){
    var hh= "hello i am being passed to view"
    var title="Page Title";
    var items= ['banana', 'apple', 'honeydew'];

    var fn = [
      {name: 'Tusty', drunkness: 3},
      {name: 'Maureen', drunkness: 10},
      {name: 'Aniqua', drunkness: 20},
      {name: 'HT', drunkness: 7}
    ];

    response.render('indexValue', {
      title: title,
      friendsName: fn,
      items: items,
      hello: hh
    });
})

//hyperlink
app.get('/link',function(request,response){
  response.send('You clicked me!');
})



app.listen(8080);
console.log("this is a sample template application")
