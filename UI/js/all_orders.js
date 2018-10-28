"use strict";

let success = document.getElementById("success");
let danger = document.getElementById("danger");
document.getElementById('all_orders').addEventListener("load", all_orders());

function all_orders() {
    fetch("https://fast-food-fast-deploy.herokuapp.com/api/v2/orders/", {
        headers: {
            'Authorization': localStorage.getItem("access_token"),
            'Accept': 'application/json',
            'Content-type': 'application/json'
        }
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            if (data.message == " There are no orders at the moment"){
                success.innerHTML = data.message
            }
            let output = ``
            data.forEach(function (all) {
                output +=
                `
                <table id="t01">
                   <tr>
                       <td>${all.orderId}</td>
                       <td>${all.item_name}</td>
                       <td>${all.quantity}</td> 
                       <td>${all.username}</td> 
                       <td>${all.status}</td>
                       <td><form  action= "update_order.html"><button id="${all.orderId}" onclick= "update_order(this.id)" class="btn complete"><span>UPDATE</span></button></form></td></td>
                    </tr>
                </table>
                `
                document.getElementById("result").innerHTML = output;
            });
        })
        .catch((err) => console.log(err))
}
