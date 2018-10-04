class Order:
    '''  Defines a Order class'''
    def __init__(self, orderId, item_name, quantity, username, status):
        ''' Initializes the order object'''
        self.orderId = orderId
        self.item_name = item_name
        self.quantity = quantity
        self.username = username
        self.status = status