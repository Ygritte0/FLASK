#-*-coding:utf-8-*-
# def show_magician(magicians):
#     magicians_name = []
#     while magicians:
#         current_magician = magicians.pop()
#         magicians_name.append(current_magician)
#     return magicians_name

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


magicians = ['alice', 'july', 'Kevin']
show_magicians(magicians)