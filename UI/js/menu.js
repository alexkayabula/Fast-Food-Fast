"use strict";

let success = document.getElementById("success");
let danger = document.getElementById("danger");
document.getElementById('menu').addEventListener("load", menu());

function menu() {
    fetch("https://fast-food-fast-deploy.herokuapp.com/api/v2/menu", {
        headers: {
            'Authorization': localStorage.getItem("access_token"),
            'Accept': 'application/json',
            'Content-type': 'application/json'
        }
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            if (data.message == " There are no food items at the moment"){
                success.innerHTML = data.message
            }
            let output = ``
            data.forEach(function (menus) {
                output +=
                `
                <table id="t01">
                   <tr>
                       <td>${menus.menu_id}</td>
                       <td>${menus.item_name}</td>
                       <td>${menus.price}</td> 
                       <td><form action= "make_order.html"><button class="btn complete"><span>ORDER</span></button></form></td>
                    </tr>
                </table>
                `
                document.getElementById("result").innerHTML = output;
            });
        })
        .catch((err) => console.log(err))
}