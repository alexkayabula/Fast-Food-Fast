"use strict"

document.getElementById('signUp').addEventListener('submit', signUp);
let success = document.getElementById("success");
let danger = document.getElementById("danger");

function signUp(e){
    e.preventDefault();

    let name = document.getElementById('name').value;
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    
    fetch("https://fast-food-fast-deploy.herokuapp.com/api/v2/auth/signup",{
      method:'POST',
      headers: {
        'Accept': 'application/json, text/plain, */*',
        'Content-type':'application/json'
      },
      body:JSON.stringify({name:name, username:username, password:password})
    })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      if ('You registered successfully. Please login.' === data.message){
        success.innerHTML=data.message;
        window.location.href = './signin.html'
        
      } else{
        danger.innerHTML=data.message;
      }
      
    })
    
  }