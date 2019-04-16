#-*-coding:utf-8-*-
def greet_users(names):
    for name in names:
        msg = "Hello," + name.title() + '!'
        print(msg)

usernames = ['alice','lyanna','john']
greet_users(usernames)