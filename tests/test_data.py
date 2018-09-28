import uuid
test_order1 = {
    "item_name": " Burger",
    "price": "25000",
    "order_date": "2018-12-12",
    "user_name": "Alex"
}

test_order2 = {
    "item_name": "Sandwich",
    "price": "16000",
    "order_date": "2018-12-12",
    "user_name": "Alex"
}

test_order3 = {
    "item_name": "Chicken",
    "price": "30000",
    "order_date": "2018-12-12",
    "user_name": "Alex"
}
test_order4 = {
    "item_name": "Chips",
    "price": "10000",
    "order_date": "2018-12-02",
    "user_name": "Alex"
}

test_order5 = {
    "item_name": "Chips",
    "price": "10000",
    "order_date": "2018-12-02",
    "user_name": "Alex"
}

past_order_date = {
    "item_name": "Egg Roll",
    "price": "5000",
    "order_date": "2017-12-12",
    "user_name": "Alex"
}

duplicate_order = {
    "item_name": "Chips",
    "price": "10000",
    "order_date": "2018-12-02",
    "user_name": "Alex"
}

test_empty_order = {
    "item_name": " ",
    "price": " ",
    "order_date": "2018-9-29",
    "user_name": " "
}

test_invalid_order1 = {
    "item_name": "chicken20",
    "price": "6000",
    "order_date": "2018-9-29",
    "user_name":  "Alex"
}


test_invalid_order2 = {
    "item_name": "chicken",
    "price": "6000",
    "order_date": "2018-9-29",
    "user_name":  "Muntu_wa_wansi"
}

test_invalid_order3 = {
    "item_name": "chicken",
    "price": "four thousand",
    "order_date": "2018-9-29",
    "user_name":  "Mozzy"
}

test_valid_order = {
    "item_name": "Chips",
    "price": "4000",
    "order_date": "2018-9-29",
    "user_name":  "Salym"
}

test_empty_key_in_order = {
    "": "chicken",
    "price": "four thousand",
    "order_date": "2018-9-29",
    "user_name":  "Mozzy"
}

test_order_id = {
        "order_id": str(uuid.uuid1()),
        "item_name": "chicken",
        "price": "four thousand",
        "order_date": "2018-9-29",
        "user_name":  "Mozzy"
        }

Orders = [{
            "order_id": str(uuid.uuid1()),
            "item_name": "chicken",
            "price": "four thousand",
            "order_date": "2018-9-29",
            "status": "Pending",
            "user_name":  "Mozzy"
        },
         {
            "order_id": str(uuid.uuid1()),
            "item_name": "chicken",
            "price": "four thousand",
            "order_date": "2018-9-29",
            "status": "Pending",
            "user_name":  "Mozzy"
        }]
