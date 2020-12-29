from typing import List
import init.eetet

def test():
    a: List[str] = [1, "s", 555, "123"]
    for i in a:
        print(i)


def test2():
    # 这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。
    # 静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言
    i: int = 1_000_000
    print(i)


def test3():
    print(r"\不专一！///")


def test4():
    if True and 1 > 0:
        print("123!!")


def test5():
    print(ord("中"))
    print(chr(25991))


def test6():
    print("动态{0}, 来了！{1}".format("语言", "我来了！"))


def test7():
    tuples: tuple[str, str] = ("124", "444455566")
    for s in tuples:
        if "124" == s:
            print(s)
            return


def test8():
    sums: int = 0
    for x in range(100):
        sums = sums + x
    print(sums)


def test9():
    pyMap: dict = dict()
    for i in range(5):
        pyMap[i] = i
    for x, y in pyMap.items():
        print(x)
        print(pyMap[y])
        # print("key={0}:value={1}".format(x, pyMap[x]))
        # print(f"key={x}:value={pyMap[x]}")

def test10():
    mySet: set = set()
    for x in range(5):
        mySet.add(x)
    mySet.add(6)
    mySet.add(1)
    for y in mySet:
        print(y)

def test11():
    i: int = int("124")
    print(i)
    x: int = max(1, 5, 19)
    print(x)

    print("124" == int)


def test12(x: int, y: int) -> int:
    # if not isinstance(x, int):
    #     raise TypeError('bad operand type')
    if not all(isinstance(item, int) for item in (x, y)):
        raise TypeError('bad operand type')
    return max(x, y)


def test13(x: int, y: int) -> tuple:
    return x, y


def test14(*number) -> int:
    sum0: int = 0
    for i in number:
        sum0 = sum0 + i
    return sum0


#可变参数 可传可不传
def test15(name, age, **kwargs):
    print('name:', name, 'age:', age, 'other:', kwargs)


def test16():

    myList: List[str] = ["123", "222", "456", "10000"]

    myListNew = myList[:3]

    print(myListNew)

    myListNew2 = myList[::2]

    print(myListNew2)

if __name__ == '__main__':

    # test()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()
    # test8()
    # test9()
    # test10()
    # test11()
    # test12(1, 2)
    # tuples: tuple = test13(1, 2)

    # numbers: List[int] = [1, 2, 3, 4, 5]
    # total: int = test14(*numbers)
    # print(total)


    #myList: List = []
    test16()

    # host = "127.0.0.1"
    # port = 7000
    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)  # 在客户端开启心跳维护
    # client.connect((host, port))
    # while True:
    #     client.send('hello world\r\n'.encode())
    #     print('send data')
    #     # 如果想验证长时间没发数据，SOCKET连接会不会断开，则可以设置时间长一点
    #     time.sleep(1)
