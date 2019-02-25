from flask import jsonify, g

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


#管理员获取用户（可以是任何人的）
@api.route('/<int:uid>',methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)

#普通用户获取信息（自己的）
@api.route('',methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)

#为了防止超权，uid从g变量中获取
@api.route('',methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


# @api.route('/create')
# def get_user():
#     return '新建用户'
#     pass
