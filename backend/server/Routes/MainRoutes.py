from flask import Blueprint

MainRoutes = Blueprint("main_Routes",__name__)

@MainRoutes.route('/')
def home():
    return "home"

