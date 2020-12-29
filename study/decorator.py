import functools


def log(fuc):
    @functools.wraps(fuc)
    def wrapper(*args, **kw):
        argList = []
        for a in args:
            argList.append(a)
        print("登录前日志！method = {0}, args = {1}".format(wrapper.__name__, argList))
        t = fuc(*args, **kw)
        print("登陆后日志！")
        _private_method()
        return t

    return wrapper


def _private_method():
    print("py里面没有私有方法, 规范是私有方法_开头！")


@log
def login(name):
    print(name + "登录了！")


if __name__ == '__main__':
    login("123")
