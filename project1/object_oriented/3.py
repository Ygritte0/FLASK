#-*-coding:utf-8--
class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()


class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)

t = Test()
t.prt()