class AdminScope:
    allow_api=['v1.super_get_user','v1.get_user']


class UserScope:
    allow_api=['v1.get_user']

def is_in_scope(scope, endpoint):

    #这里是根据一个类的名字获取对应的实例。
    #  globals() 比较有意思，他返回的是一个字典，包含了当前的各种类啊什么的
    scope = globals()[scope]()

    print(scope.allow_api)

    if endpoint in scope.allow_api:
        return True
    else:
        return False


