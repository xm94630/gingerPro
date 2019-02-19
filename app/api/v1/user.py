from app.libs.redprint import Redprint
from app.libs.token_auth import auth

#from flask import Blueprint

# blueprint
# user = Blueprint('user',__name__)

# redprint



api = Redprint('user')

@api.route('/get')
@auth.login_required
def get_user():
    return '泰罗'

# @api.route('/create')
# def get_user():
#     return '新建用户'
#     pass
