"use strict"

document.getElementById('add_menu_item').addEventListener('submit', add_menu_item);
function add_menu_item(e){
    e.preventDefault();

    let item_name = document.getElementById('item_name').value;
    let price = document.getElementById('price').value;

    fetch("https://fast-food-fast-deploy.herokuapp.com/api/v2/menu", {
      method:'POST',
      headers: {
        'Authorization':localStorage.getItem("access_token"),
        'Accept': 'application/json, text/plain, */*',
        'Content-type':'application/json'
      },
      body:JSON.stringify({item_name:item_name, price:price})
    })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      if (data.message === "You added a food item successfully."){
        success.innerHTML = data.message
        window.location.href = './menu.html'
      }else{
        danger.innerHTML = data.message
      }

    })
  }