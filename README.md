# Fast Food Fast
Fast-Food-Fast is a food delivery service app for a restaurant.

# Features 

- Users can create an account and log in
- A user should be able to order for food
- The admin should be able to add,edit or delete the fast-food items
- The admin should be able to see a list of fast-food items
- The Admin user should be able to do the following:
- See a list of orders
- Accept and decline orders
- Mark orders as completed
- A user should be able to see a history of ordered food

# EndPoints
    
    EndPoint                                           | Functionality
    ------------------------                           | ----------------------
    POST /auth/register                                | Create a user account
    POST /auth/login                                   | Login a user
    POST /users/orders/                                | Place and order for food
    GET  /users/orders                                 | Get order history for a particular user
    GET  /orders/                                      | Get all orders, Admin access only
    POST /orders/<orderId>                             | Fetch a specific order, Admin access only
    PUT  /orders/rides/<orderId>                       | Update the status of an order, Admin access
    GET  /menu                                         | Get available menu, Admin access only
    POST /menu                                         | Add a meal option to menu, Admin access only

# Technologies Used 

* [Flask](http://flask.pocoo.org/)

* [Python 3.6](https://docs.python.org/3/)

* [PostgreSQL](https://www.postgresql.org/)


# Installation

Clone this repository
- git clone https://github.com/alexkayabula/Fast-Food-Fast.git

Create a virtual environment
- python -m venv env

Install the dependencies
 - pip install -r requirements.txt

# Unittesting
- nosetests --with-coverage --cover-package=app && coverage report`