from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm, UserEmailForm
from app.models.user import User

api = Redprint('clinet')

#用于客户端注册的
# 注册、登录
@api.route('/register',methods=['POST'])
def create_client():

    # 校验参数
    # 表单用WTForms来校验

    # 主要这里我们使用表单form的形式提交数据，除此之外还有json
    # 我们再postman工具中可以看到，有很多提交的类型
    # form-data就是表单、raw+JSON(application/json)是json的类型
    # 网页中多为表单、微信小程序中多为json

    # 从客户端接受参数有两种类型
    # request.json
    # request.args.to_dict()

    data = request.json

    # 注意这里data=data的用法（这是针对request.json类型）
    # 我这里特意查了下这种用法，这种叫做关键字参数用法
    # 函数定义的时候，用**来表示这种特定的参数，如 def fun(a,b,**others):

    form = ClientForm().validate_for_api()

    # 注意这里promise只是个字典而已
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()

    #這裡為什麼可以return這個呢，因為它本質上是一個HTTPException
    #經驗：我們可以接受定義時候的複雜，但是不能接受調用的時候的複雜
    return Success()



def __register_user_by_email():
    print ("准备写入数据库哦")
    form = UserEmailForm().validate_for_api()
    print('数据格式验证成功！')
    User.register_by_email(form.nickname.data,form.account.data,form.secret.data)
