# -*-coding:utf-8--
class MyClass:
    """一个简单的实例"""
    i = 12345
    def f(self):
        return 'hello world'

#实例化类
x = MyClass()

# 访问类的属性和方法
print('Myclass 类的属性 i 为：', x.i)
print('Myclass 类的方法 f 为：', x.f())
