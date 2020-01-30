function toggleNav()
{
    currentWidth = document.getElementById("sideMenu").style.width;
    newWidth = currentWidth == "250px" ? "0" : "250px";
    document.getElementById("sideMenu").style.width = newWidth;
}

function closeNav()
{
    document.getElementById("sideMenu").style.width = "0";
} 

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function getAnswer(questID) {

    //We disabled all radio buttons after the user validate his answer 
    var choiceField = document.getElementById("id_choice_field");
    var inputInChoiceField = choiceField.getElementsByTagName("input");
    inputInChoiceField[0].disabled = true;
    inputInChoiceField[1].disabled = true;
    inputInChoiceField[2].disabled = true;
    //ID of the answer selected by the user 
    answID = document.querySelector('input[name="choice_field"]:checked').value;
    document.querySelector('input[name="choice_field"]:checked').parentElement.parentElement.style.backgroundColor = "#0DFF92" ; 
    
    //Handle the response of the server
    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        //We take all the dataset of server's response 
        var responseObject = JSON.parse(this.responseText);
        var goodAnswerBool = responseObject["goodAnswerBool"] ; 
        var goodAnswerID = responseObject["goodAnswerID"] ; 
        //Compute the server's responses : 
        if(true == goodAnswerBool)
        {
            console.log("Bonne Réponse");
        }
        else {
            console.log("Mauvaise Réponse");
        }
      }
    };
    //Request to the server
    xhttp.open("POST", "", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("questionID=" + questID + "&answerID=" + answID + "&csrfmiddlewaretoken=" + csrftoken );
}  

function changeColorChoice(el)
{
    if(el.parentElement.parentElement.style.backgroundColor == "#FFFFFF")
    {
        el.parentElement.parentElement.style.backgroundColor = "#0DFF92" ; 
    }
    else {
        el.parentElement.parentElement.style.backgroundColor = "#FFFFFF" ; 
    }
    //document.querySelectorAll('input[name="choice_field"]').parentElement.parentElement.style.backgroundColor = "#FFFFFF" ; 
    //document.querySelectorAll('li').style.backgroundColor = "#FFFFFF" ;
    //document.querySelector('input[name="choice_field"]:checked').parentElement.parentElement.style.backgroundColor = "#0DFF92" ; 
}