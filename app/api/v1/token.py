from flask import current_app, jsonify

from app.config.setting import TOKEN_EXPIRATION
from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm
from models.user import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

api = Redprint('token')

#登录，其实就是为了拿到token;另外这里按照REST用的get，但是我们要违背下
@api.route('',methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify
    }

    #验证身份通过，也成功拿到用户的id
    identify = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )

    #下一步就是生成令牌
    #令牌是需要加密的，会涉及到加密的算法，flask自带了一个 itsdangerous 库，方便我们去生成令牌
    expiration = current_app.config['TOKEN_EXPIRATION'],
    token = generate_auth_token(
        identify['uid'],
        form.type.data,
        None,
        expiration
    )

    t = {
        "token":token.decode('ascii') #这不是普通的字符串，还需要decode下
    }
    return jsonify(t),201


#令牌除了加密，还要写入用户的信息：用户id、客户端种类、权限作用域（暂时不用），过期时间
def generate_auth_token(uid,ac_type,scope=None,expiration=7200):
    #生成令牌
    s = Serializer(
        current_app.config['SECRET_KEY'],   # 只有 SECRET_KEY 才能解开令牌
        expires_in= expiration              # 令牌有效期
    )
    #写入信息，最后生成的是一个字符串，就是我们的token令牌
    return s.dump({
        'uid':uid,
        'type':ac_type.value
    })

