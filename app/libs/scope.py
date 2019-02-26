class Scope:
    # def add(self,other):
    #     self.allow_api = self.allow_api + other.allow_api
    #     return self

    #运算符重置，__add__是内置的方法。相当于都"+"号做了新的定义
    def __add__(self,other):
        self.allow_api = self.allow_api + other.allow_api
        return self


class AdminScope(Scope):
    allow_api=['v1.super_get_user']
    def __init__(self,):
        #self.add(UserScope())
        self+UserScope()
        print('==1')
        print(self.allow_api)

class UserScope(Scope):
    allow_api=['v1.get_user']

class SuperScope(Scope):
    allow_api =['v1.xxxxxxx']
    def __init__(self,):
        #self.add(UserScope()).add(AdminScope())
        self+UserScope()+AdminScope()
        print('==2')
        print(self.allow_api)

SuperScope()
AdminScope()


def is_in_scope(scope, endpoint):

    #这里是根据一个类的名字获取对应的实例。
    #  globals() 比较有意思，他返回的是一个字典，包含了当前的各种类啊什么的
    scope = globals()[scope]()

    print(scope.allow_api)

    if endpoint in scope.allow_api:
        return True
    else:
        return False


