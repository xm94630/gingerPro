
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder


class JSONEncoder(_JSONEncoder):
    print('====???????????')
    def default(self,o):
        print('kkkkkkkkkkkkkkkk')
        return dict(o)


class Flask(_Flask):
    print('===---->')
    json_encoder = JSONEncoder

def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(),url_prefix='/v1')

def register_plugin(app):
    from models.base import db
    db.init_app(app)  #插件注册
    with app.app_context(): #推入上下文环境
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprints(app)
    register_plugin(app)

    print('xxx')

    return app

