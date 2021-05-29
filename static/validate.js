function reg_validate(){
  console.log("Started Function")
  var username = document.forms["register-form"]["username"].value;
  var password = document.forms["register-form"]["password"].value;
  var confirm = document.forms["register-form"]["confirm"].value;
  console.log("Running Validate Function")
  console.log(username+" "+password+" "+confirm)
  if(username=="" || password=="" || confirm==""){
    alert("Empty Fields");
    return false;
  }
  else if(password!=confirm){
    alert("Password dosent match!")
    return false;
  }
  else{
    return true;
  }
}

function login_validate(){
  console.log("Started Function")
  var username = document.forms["register-form"]["username"].value;
  var password = document.forms["register-form"]["password"].value;
  if(username=="" || password==""){
    alert("Empty Fields");
    return false;
  }
  else{
    return true;
  }
}