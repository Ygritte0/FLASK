#-*-coding:utf-8-*-
# 编写一个名为make_shirt() 的函数，
# 它接受一个尺码以及要印到T恤上的字样。 这个函数应打印一个句子， 概要地说明T恤的尺码和字样。
def make_shirt(shirt_size, shirt_logo):
    print("The shirt's size is : %s"% shirt_size)
    print("The shirt's logo is : %s"% shirt_logo)


make_shirt("M","Victory")

# 8-4
def make_shirt( shirt_logo,shirt_size="L"):
    print("The shirt's size is : %s" % shirt_size)
    print("The shirt's logo is : %s" % shirt_logo)

make_shirt("Win!")

# 8-5
def make_shirt(shirt_size, shirt_logo="I love python."):
    print("The shirt's size is : %s" % shirt_size)
    print("The shirt's logo is : %s" % shirt_logo)

make_shirt("S")


# 让实参变成可选的
def get_formatted_name (first_name, last_name, middle_name=""):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

print(get_formatted_name('jucy', 'smith', 'lee'))

# 定义一个人的信息，并用字典返回
def person(first_name, last_name, age=''):
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

print(person('andy', 'green', age=13))