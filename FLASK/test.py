class A:
    a = 'c'

    def __init__(self, value):
        self.value = value

    @classmethod
    def get_a(cls):
        return cls.a

    def get_value(self):
        return self.value

    @property
    def name(self):
        print('get name')
        return self.value

    @name.setter
    def name(self, value):
        print('set name')
        self.value = value

if __name__ == '__main__':

    # print(A.a)
    print(A.get_a())


    # a = A('b')
    # print(a.get_value())

    # a.value == 'b'
    #
    # a.name == 'b'
    #
    # a.name = 'c'
    #
    # a.name == 'b'
