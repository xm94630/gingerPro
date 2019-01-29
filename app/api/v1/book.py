from app.libs.redprint import Redprint

#from flask import Blueprint

# blueprint
#book = Blueprint('book',__name__)

# redprint
api = Redprint('book')

print('===>')

@api.route('/get')
def get_book():
    return 'get book';

@api.route('/create')
def create_book():
    return 'create book';