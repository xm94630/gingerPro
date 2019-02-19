
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):
    #这个函数是会被递归调用的，遇到不能序列化的层级的时候，都会再进来处理
    def default(self,o):
        if hasattr(o,'keys') and hasattr(o,'__getitem__'):
            return dict(o)
        raise ServerError()

class Flask(_Flask):
    json_encoder = JSONEncoder
