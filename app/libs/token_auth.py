from collections import namedtuple

from flask import current_app,g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed

auth = HTTPBasicAuth()

#这种类型的，类似list，值不能被改变，还用通过名字访问
User = namedtuple('User',['uid','ac_type','is_admin'])

@auth.verify_password
def verify_password(token,password):
    print('===>')
    print(token)

    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        #这里的g同request一样，都是代理模式的实现。
        print('===>2')
        print(user_info)
        g.user = user_info
        return True

def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg="token is invalid(哦)",error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg="token is expired(过期啦)", error_code=1003)

    uid = data['uid']
    ac_type = data['type']
    is_admin = data['is_admin']

    return User(uid,ac_type,is_admin)