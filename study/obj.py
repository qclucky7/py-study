from study import conifg


class User(object):
    # 用tuple定义允许绑定的属性名称 限定后只能传这两个参数, 要不可以加任意参数
    __slots__ = ('__name', '__age', "__score")

    # __修饰变量为私有变量
    def __init__(self, name: str, age: int):
        self.__score = 0
        self.__name = name
        self.__age = age

    #
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value

    def print(self):
        print("name={0}, age={1}, score={2}".format(self.__name, self.__age, self.__score))

    def __str__(self) -> str:
        return "User: name={0}, age={1}, score={2}".format(self.__name, self.__age, self.__score)


if __name__ == '__main__':
    user: User = User("王晨", 24)
    # user.score = "123"
    user.score = 33
    #user.print()
    print(user)
    print(conifg.Constant.__version__)
    print(conifg.Constant.__application_name__)
