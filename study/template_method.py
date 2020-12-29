from study import conifg
import abc


class AbstractExecute(object):

    def exec(self):
        if self.hook():
            print("父类执行器")
        else:
            print("不执行父类执行器")

    @abc.abstractmethod
    def hook(self):
        return True

    @staticmethod
    def version():
        return conifg.Constant.__version__


def dynamic_method():
    print("动态方法动态绑定！")


class DefaultExecutor(AbstractExecute):

    def hook(self):
        return True


# def hook(self):
    #     return True


if __name__ == '__main__':
    executor: AbstractExecute = DefaultExecutor()
    print(executor.version())
    executor.exec()


    print(type(executor))
    print(isinstance(executor, AbstractExecute))
