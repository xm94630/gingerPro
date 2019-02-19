from http.client import HTTPException
from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

app = create_app();

# @app.route('/v1/user/get')
# def get_user():
#     return 'i am qiyue'
#
# @app.route('/v1/book/get')
# def get_book():
#     return 'book';


@app.errorhandler(Exception)
def framework_error(e):
      if isinstance(e,APIException):
          # 参数中type号码有误的时候，走这个
          return e
      if isinstance(e,HTTPException):
          code = e.code
          msg = e.description
          error_code = 1007
          return APIException(msg,code,error_code)
      else:
          # 把 localhost:5000/v1/clinet/register 的post方法改成get走的是这个，不是七月说的第二个逻辑
          # create_client方法中，出现"0/0"也是这个逻辑
          if not app.config['DEBUG']:
              return ServerError()
          else:
              raise e

if __name__ == '__main__':
    app.run(debug=True)