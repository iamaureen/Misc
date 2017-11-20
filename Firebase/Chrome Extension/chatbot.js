
window.onload = function() {

    document.getElementById('inputbtn').addEventListener('click', getResponse);

};


function getResponse(){
  var userInput = document.getElementById('input').value;
  console.log(userInput)

  userInput = {
    'question': userInput
  }

  userInput = JSON.stringify(userInput)
  console.log(userInput)

  $.ajax({
     type: 'POST',
     beforeSend: function(request) {
        request.setRequestHeader("Ocp-Apim-Subscription-Key", 'fb94616c0e334be1a9a6420d2ecb1a77');
    },
     contentType: 'application/json',
     url: 'https://westus.api.cognitive.microsoft.com/qnamaker/v2.0/knowledgebases/a341008b-98d2-4ba2-b17d-152289a52bb0/generateAnswer',
     data: userInput,
     dataType: 'json',
     success: function (dataObj, textStatus, xhr) {

       console.log(dataObj)

       //get the response from the chatbot
       console.log(dataObj['answers'][0].answer)
       var response = dataObj['answers'][0].answer;
       document.getElementById("chatbox").value = response
       },
       error: function (xhr, textStatus, errorThrown) {
                 console.log(xhr);
       }

   });

}
