from flask import Blueprint

Auth_Routes = Blueprint("Auth_Routes",__name__)

@Auth_Routes.route("/Login")
def Login():
    return "Login"

@Auth_Routes.route('/signup')
def signup():
    return 'Signup'

@Auth_Routes.route('/logout')
def logout():
    return 'Logout'