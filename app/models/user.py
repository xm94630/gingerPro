#直接复制

from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import NotFound, AuthFailed


#from app.models.base import Base, db, MixinJSONSerializer
from app.models.base import Base, db


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(100))

    def keys(self):
        return ['id', 'email', 'nickname', 'auth']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname, account, secret):

        #xm:with语法用于上下文管理协议
        #例如，我们原先这样子的写法
        # file = open("/tmp/foo.txt")
        # try:
        #     data = file.read()
        # finally:
        #     file.close()

        #可以该写成：
        # with open("/tmp/foo.txt")
        #   as file:
        #     data = file.read()


        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    #验证
    @staticmethod
    def verify(email, password):
        # user = User.query.filter_by(email=email).first_or_404()
        # if not user.check_password(password):
        #     raise AuthFailed()
        # scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        # return {'uid': user.id, 'scope': scope}

        user = User.query.filter_by(email=email).first()
        if not user:
            raise NotFound(msg="user not found")
        if not user.check_password(password):
            raise AuthFailed()

        scope = 'AdminScope' if user.auth ==2 else 'UserScope'
        print('--------->user.auth')
        print(user.auth)
        print('--------->scope')
        print(scope)

        return {'uid': user.id,'scope':scope}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    # def _set_fields(self):
    #     # self._exclude = ['_password']
    #     self._fields = ['_password', 'nickname']
