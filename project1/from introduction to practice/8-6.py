#-*-coding:utf-8-*-
def city_country(city_name, country_name):
    total = city_name.title() + ' ' + 'is in' + ' '+ country_name.title()
    return total

print(city_country('Beijing','China'))
print(city_country('toronto','canada'))
print(city_country('new york','america'))

def make_album(singer_name,album_name,songs_count='10'):
    album = {'s':singer_name,'a':album_name,'counts':songs_count}
    return album
while True:
    print("Please enter 'q' at any time to quit.")
    s_name = input('s:')
    if s_name == 'q':
        break
    a_name = input('a:')
    if a_name == 'q':
        break
    # info_of_album = make_album(s_name,a_name)
    print(make_album(s_name,a_name))


# print(make_album('Talor','Red'))
# print(make_album('Talor','22'))
# print(make_album('Talor','1989'))