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


class People(object):
    can_breath = True
    can_see = True
    can_fly = False

    def __init__(self, can_smoke, can_play_basketball, second_name='', first_name=''):
        self.can_smoke = can_smoke
        self.can_play_basketball = can_play_basketball
        self.second_name = second_name
        self.first_name = first_name

    @property
    def name(self):
        return self.second_name + ' ' + self.first_name

    @name.setter
    def name(self, fullname):
        second_name, first_name = fullname.split(' ')
        self.first_name = first_name
        self.second_name = second_name

    def learn_smoke(self):
        self.can_smoke = True

    @classmethod
    def evolute(cls):
        cls.can_fly = True

    @staticmethod
    def sum(a, b):
        return a + b


if __name__ == '__main__':
    # print('can_fly: ', People.can_fly)
    #
    # zm = People(False, False)
    # print('can_fly: ', zm.can_fly)
    #
    # People.evolute()
    # print('evolute')
    # print('can_fly: ', People.can_fly)
    # print('can_fly: ', zm.can_fly)
    #
    # zjw = People(False, False)
    # print('can_fly: ', zjw.can_fly)

    zm = People(False, False, 'zhao', 'meng')

    print(zm.name)

    # zm.name = 'zhu jiawei'
    # fullname = 'zhu jiawei'
    # second_name, first_name = fullname.split(' ')
    # zm.first_name = first_name
    # zm.second_name = second_name

    zm.name = 'zhu jiawei'
    print('zm first name: ', zm.first_name)
    print('zm second name: ', zm.second_name)

    # a = A('b')
    # print(a.get_value())

    # a.value == 'b'
    #
    # a.name == 'b'
    #
    # a.name = 'c'
    #
    # a.name == 'b'
    pass
