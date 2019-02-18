from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm
from models.user import User

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



    pass