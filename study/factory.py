import enum


@enum.unique
class ParseType(enum.Enum):
    # xml pars
    XML = 0
    # json parse
    JSON = 1


class XmlParser(object):

    def __init__(self):
        print("XmlParser init!")
        pass

    def parse(self):
        print("xml解析！")

    def __del__(self):
        print("XmlParser del!")


class JsonParser(object):

    def parse(self):
        #raise ex.CustomException("自定义异常")
        print("json解析！")


class ParseFactory(object):

    @staticmethod
    def get(type_: ParseType):
        if ParseType.XML == type_:
            return XmlParser()
        if ParseType.JSON == type_:
            return JsonParser()


if __name__ == '__main__':
    ParseFactory.get(ParseType.XML).parse()
