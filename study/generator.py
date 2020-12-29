def test1():
    for i in range(1, 5):
        yield i


def test2():
    yield 123
    yield from test1()
    yield 46


print(test2())

# def test_generator(max: int):
#     n = 0
#     while n < max:
#         yield n
#         n = n + 1
#
#
# def fib(max: int):
#     n, a, b = (0, 0, 1)
#     while n < max:
#         yield b
#         a, b = (b, a + b)
#         n = n + 1
#
#
# if __name__ == '__main__':
#     # for x in test_generator(5):
#     #     print(x)
#
#     for x in fib(10):
#         print(x)
