from flask_wtf import Form

#快速导入快捷键的方法
# 1 鼠标停留到 form，使用快捷键 alt+enter
# 2 鼠标点击报错的红叹号
from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self,data):
        super(BaseForm,self).__init__(data=data)

    def validate_for_api(self):
        valid = super(BaseForm,self).validate()
        if not valid:
            #验证错误的信息全部放在errors中
            raise ParameterException(msg=self.errors)
