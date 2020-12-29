# 变量
# 单下划线 _xxx 包私有 protected
# 双下划线 __xxx 类私有 private
# 双下划线开头和结尾 __xxx___ 系统内置变量


# 函数
# _fuc 私有方法
# __fuc___ 双下划线开头结尾  魔术方法
# fuc 一般方法


# 类
# 1. 驼峰命名 MyClass
# 2. 基类 用Base或者Abstract开头


import requests


if __name__ == '__main__':
    requests.api.get()