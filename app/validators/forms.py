from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError

from app.libs.enums import ClientTypeEnum
from models.user import User


class ClientForm(Form):

    account = StringField(validators=[DataRequired(),length(min=5,max=32)])
    secret  = StringField()
    type    = IntegerField()

    #注意，这个函數會被自動調用，應該在父類中也有，這裡是做了覆蓋。
    #self类似于js中的this，只是js中直接用就行了
    def validate_type(self,value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data  = client



# （这部分复制的）
# 利用继承减少代码
class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        # password can only include letters , numbers and "_"
        #Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()