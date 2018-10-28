'use strict'

document.getElementById('login').addEventListener('submit', login);
  
function login(e){
    e.preventDefault();
  
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
  
    fetch("https://fast-food-fast-deploy.herokuapp.com/api/v2/auth/login",{
      method:'POST',
      headers: {
        'Accept': 'application/json, text/plain, */*',
        'Content-type':'application/json'
      },
      body:JSON.stringify({username:username, password:password})
    })
    .then((response) => response.json())
    .then((data) => {
      
      
      if("token" in data){
      
        localStorage.setItem("access_token", data.token);
        localStorage.setItem("username", username);
        if (username === 'admin')
            document.getElementById("message").innerHTML=data.message;
            window.location.href = './admin_profile.html'
        if (username !== 'admin'){
            document.getElementById("message").innerHTML=data.message;
            window.location.href = './user_profile.html'
        }
          
      }
      console.log(data);
      document.getElementById("message").innerHTML=data.message;
        
    })
      
  }