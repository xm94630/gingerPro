from app.libs.redprint import Redprint
#from flask import Blueprint

# blueprint
# user = Blueprint('user',__name__)

# redprint
api = Redprint('user')

@api.route('/get')
def get_user():
    return '泰罗'
