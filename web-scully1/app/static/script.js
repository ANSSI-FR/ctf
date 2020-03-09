//Using our API

function login(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    var dat = {'username':username, 'password':password};

    $.ajax('/api/v1/login/',{
        method: 'POST',
        data: JSON.stringify(dat),
        dataType: "json",
        contentType: "application/json",
    }).done(function(res){

      if (res['status'] == 'success'){
        $("#stat").html('<b>Successful Login. Here is your flag: ');
        $("#stat").append(res['flag']);
        $("#stat").append('</b>');
      }
      else{
        $("#stat").html('<b>Login Failed</b>');
      }

    }).fail(function(err){
        $("#stat").html(err);
    });
}

$(document).ready(function(){

    $("#navbar ul li a").on('click', function(event){
        event.preventDefault();
        var page = $(this).attr("href");

        $("#main").load(page);
    });
});
