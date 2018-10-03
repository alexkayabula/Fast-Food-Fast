"""Handles adding endponts to the blueprints"""
from flask import Blueprint
from app.menu.api import MenuView

MENU_BLUEPRINT = Blueprint('menu', __name__)
MENU_VIEW = MenuView.as_view('MENU_VIEW')
MENU_BLUEPRINT.add_url_rule('/api/v2/menu', view_func=MENU_VIEW, methods=['POST'])
MENU_BLUEPRINT.add_url_rule('/api/v2/menu', view_func=MENU_VIEW, methods=['GET'])