
from app.app import create_app
app = create_app();

# @app.route('/v1/user/get')
# def get_user():
#     return 'i am qiyue'
#
# @app.route('/v1/book/get')
# def get_book():
#     return 'book';

if __name__ == '__main__':
    app.run(debug=True)