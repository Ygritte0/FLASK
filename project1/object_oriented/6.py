# -*-coding:utf-8--
class People:
    # name = ''
    # age = 0
    # __weight = 0

    def __init__(self, n='', a=0, w=0, bf=None):
        self.name = n
        self.age = a
        self.__weight = w
        self.bf = bf

    def speak(self):
        print("%s 说：我 %d 岁。" % (self.name, self.age))

zjw = People('zjw')

zm = People(bf=zjw)
zm2 = People(zjw)


print(zm.bf is zjw)


class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print("%s 说：我在度 %d 年级。" % (self.name, self.grade))


class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s,我是一个演说家，我演讲的主题是 %s ." % (self.name, self.topic))


class sample(speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)

        # test = sample("Tim", 25,80,4,"Python")
        # test.speak()
