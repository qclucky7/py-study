

def test_for():
    for x in [1, 2, 3]:
        print(x)

    for index, value in enumerate([1, 2, 3]):
        print("index = {0}, value = {1}".format(index, value))


def dict_for():

    myDict: dict = {}

    myDict.setdefault(1, 2)
    myDict.setdefault(2, 3)



    for k, y in myDict.items():
        print("key = {0}, value = {1}".format(k, y))


if __name__ == '__main__':
     test_for()
    # dict_for()
