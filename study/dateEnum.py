from enum import Enum, unique


@unique
class DateEnum(Enum):
    ONCE = 0

    TWO = 1


if __name__ == '__main__':
    print(DateEnum.ONCE.name)
    print(DateEnum.ONCE.value)
