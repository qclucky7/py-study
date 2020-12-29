import requests

if __name__ == '__main__':

    requests.get()
    try:
        1 / 0
    except BaseException as ex:
        print(ex)
    finally:
        print("finally!")


class CustomException(BaseException):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
