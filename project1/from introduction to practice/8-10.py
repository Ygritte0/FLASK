#-*-coding:utf-8-*-
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    great_magicians = []
    # 让每一个magician变成magician the great,并加入great_magicians
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' '+ 'the Great'
        great_magicians.append(great_magician)
    # 此时，magicians 的列表已经是空列表了，把加完the great的“great magicians”再次加到magicians 列表里
    for great_magician in great_magicians:
        magicians.append(great_magician)


magicians = ['Alice', 'July', 'Kevin']
# 此处是为了和下面的show_magicians(magicians)对比????
show_magicians(magicians)

# 调用make_great(magicians)函数
make_great(magicians)
# 因为14行把magician the great 加回到magicians了，所以调用完make_great还得调用show_magicians函数
show_magicians(magicians)