"use strict"

document.getElementById('make_order').addEventListener('submit', make_order);
function make_order(e){
    e.preventDefault();

    let item_name = document.getElementById('item_name').value;
    let quantity = document.getElementById('quantity').value;

    fetch("https://fast-food-fast-deploy.herokuapp.com/api/v2/users/orders", {
      method:'POST',
      headers: {
        'Authorization':localStorage.getItem("access_token"),
        'Accept': 'application/json, text/plain, */*',
        'Content-type':'application/json'
      },
      body:JSON.stringify({item_name:item_name, quantity:quantity})
    })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      if (data.message === "You have placed an order successfully."){
        success.innerHTML = data.message
        window.location.href = './order_history.html'
      }else{
        danger.innerHTML = data.message
      }

    })
  }