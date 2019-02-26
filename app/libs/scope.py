class Scope:
    allow_api=[]
    allow_module = []
    forbidden = []

    # def add(self,other):
    #     self.allow_api = self.allow_api + other.allow_api
    #     return self

    #运算符重置，__add__是内置的方法。相当于都"+"号做了新的定义
    def __add__(self,other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))          # set 定义集合元素，不重复，相当于去重
        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))
        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))
        return self


class AdminScope(Scope):
    allow_api=['v1.super_get_user','v1.super_delete_user']
    allow_module = ['v1.user']
    def __init__(self,):
        #self.add(UserScope())
        #self+UserScope()
        print('==1')
        print(self.allow_api)

class UserScope(Scope):
    #allow_api=['v1.user+get_user','v1.user+delete_user']

    forbidden = ['v1.super_get_user','v1.super_delete_user']
    def __init__(self):
        self + AdminScope()

# class SuperScope(Scope):
#     allow_api =['v1.xxxxxxx']
#     allow_module = ['v1.user']
#
#     def __init__(self,):
#         #self.add(UserScope()).add(AdminScope())
#         self+UserScope()+AdminScope()
#         print('==2')
#         print(self.allow_api)




def is_in_scope(scope, endpoint):

    #这里是根据一个类的名字获取对应的实例。
    #  globals() 比较有意思，他返回的是一个字典，包含了当前的各种类啊什么的
    scope = globals()[scope]()

    #这里 scope.allow_api 保存了 "v1.view_func" 这样子的视图函数，我们需要改变它默认的，中间添加 module 的名字
    #这样子为了权限控制的时候，对整个模块的下的视图函数的支持，而不用一个一个的添加。
    #我们需要 scope.allow_api 改成 "v1.模块名字(也就是红图的名字)+view_func"这样的形式
    splits = endpoint.split('+')
    red_name = splits[0]

    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return  True

    else:
        return False


