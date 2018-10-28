"use strict"


document.getElementById('update_order').addEventListener('submit', update_order);

function update_order(e, orderId){
    e.preventDefault()
    let status = document.getElementById('status').value;
    localStorage.setItem('id', orderId);
    fetch(`https://fast-food-fast-deploy.herokuapp.com/api/v2/orders/${orderId}`, {
      method:'PUT',
      headers: {
        'Authorization':localStorage.getItem("access_token"),
        'Accept': 'application/json, text/plain, */*',
        'Content-type':'application/json'
      },
      body:JSON.stringify({status:status})
    })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      if (data.message === "Order not Found"){
       danger.innerHTML = data.message  
      }
      if (data.message === "Invalid Status"){
        danger.innerHTML = data.message  
       }
      else{
        success.innerHTML = "The order has been updated successfully"
      }
    })
  }