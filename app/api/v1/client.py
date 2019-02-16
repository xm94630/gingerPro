from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm, UserEmailForm
from models.user import User

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
    form = ClientForm(data=data)  #助理这里data=data的用法（这是针对request.json类型）
    if form.validate():
        # 注意这里promise只是个字典而已
        promise = {
            ClientTypeEnum.USER_EMAIL:__register_user_by_email
        }
        promise[form.type.data]()

        print('成功啦')
        return 'success'
    else:
        return '格式有问题哦，亲'



def __register_user_by_email():
    print ("准备写入数据库哦")
    form = UserEmailForm(data=request.json)
    print(form)
    print(form.validate())
    if form.validate():
        print('数据格式验证成功！')
        User.register_by_email(form.nickname.data,form.account.data,form.secret.data)
