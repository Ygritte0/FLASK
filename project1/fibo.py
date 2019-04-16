#-*-coding:utf-8--

a = {'a': 1}

def print_a():
    print(a)

def fib(n):
    print(1 + 'a')
    a, b = 0,1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

print("python's __name__ value is: %s, type is: %s" % (__name__, type(__name__)))

if __name__ == '__main__':
    print('executing fibo.py', fib2(2))
