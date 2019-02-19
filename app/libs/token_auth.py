from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(account,password):
    print('===>')
    print(account)
    print(password)
    return True