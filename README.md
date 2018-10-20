[![Build Status](https://travis-ci.org/alexkayabula/Fast-Food-Fast.svg?branch=Back-up)](https://travis-ci.org/alexkayabula/Fast-Food-Fast)
[![Maintainability](https://api.codeclimate.com/v1/badges/3c3c2c844f0852897484/maintainability)](https://codeclimate.com/github/alexkayabula/Fast-Food-Fast/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/alexkayabula/Fast-Food-Fast/badge.svg)](https://coveralls.io/github/alexkayabula/Fast-Food-Fast)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/dd3c7a4fb0b64824844de46420548c6a)](https://www.codacy.com/app/alexkayabula/Fast-Food-Fast?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=alexkayabula/Fast-Food-Fast&amp;utm_campaign=Badge_Grade)

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

# Unittesting and Coverage Reports
- nosetests --with-coverage --cover-package=app && coverage report
- coverage report
- coverage html -i

# Hosting
- https://fast-food-fast-deploy.herokuapp.com/api/v2/signup