class Manager(object):

    def __init__(self, name: str = 123):
        self.name = name

    def __enter__(self):
        print("enter方法！")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit方法: type={0}, val={1}, tb={2}".format(exc_type, exc_val, exc_tb))


if __name__ == '__main__':
    with Manager() as manager:
        print("123")
