from flask import jsonify

from app.libs.error_code import DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth

#from flask import Blueprint

# blueprint
# user = Blueprint('user',__name__)

# redprint
from models.base import db
from models.user import User

api = Redprint('user')


class QiYue:
    name="xxx"
    age=99

    def __init__(self):
        self.gender = 'male'

    def keys(self):
        return ['name','age','gender']

    def __getitem__(self,item):
        return getattr(self,item)


@api.route('/<int:uid>')
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    r = {
        'nickname':user.nickname,
        'email':user.email
    }
    #return jsonify(r)
    #return jsonify(QiYue())
    return jsonify(user)


@api.route('/<int:uid>',methods=['DELETE'])
@auth.login_required
def delete_user(uid):
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


# @api.route('/create')
# def get_user():
#     return '新建用户'
#     pass
