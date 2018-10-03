"""Handles adding endponts to the blueprints"""
from flask import Blueprint
from app.order.api import OrderView

ORDER_BLUEPRINT = Blueprint('order', __name__)
ORDER_VIEW = OrderView.as_view('ORDER_VIEW')
ORDER_BLUEPRINT.add_url_rule('/api/v2/users/orders', view_func=ORDER_VIEW, methods=['POST'])
ORDER_BLUEPRINT.add_url_rule('/api/v2/users/orders', view_func=ORDER_VIEW, methods=['GET'])