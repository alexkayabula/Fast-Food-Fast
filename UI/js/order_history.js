"use strict";

let success = document.getElementById("success");
let danger = document.getElementById("danger");
document.getElementById('my_orders').addEventListener("load", my_orders());

function my_orders() {
    fetch("https://fast-food-fast-deploy.herokuapp.com/api/v2/users/orders", {
        headers: {
            'Authorization': localStorage.getItem("access_token"),
            'Accept': 'application/json',
            'Content-type': 'application/json'
        }
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            if (data.message == "You have not placed any orders"){
                success.innerHTML = data.message
            }
            let output = ``
            data.forEach(function (orders) {
                output +=
                `
                <table id="t01">
                   <tr>
                       <td>${orders.orderId}</td>
                       <td>${orders.item_name}</td>
                       <td>${orders.quantity}</td> 
                       <td>${orders.username}</td> 
                       <td>${orders.status}</td> 
                    </tr>
                </table>
                `
                document.getElementById("result").innerHTML = output;
            });
        })
        .catch((err) => console.log(err))
}