#-*-coding:utf-8-*-
def make_album(singer_name, album_name, songs_count='10'):
    info_of_album = {'Author':singer_name, 'album':album_name,'how many songs':songs_count}
    return info_of_album




while True:
    print("Please tell me your favorite singer's name:")
    print("(Enter 'q' at any time to quit.)")
    s_name = input('singer_name:')
    if s_name == 'q':
        break
    a_name = input('album_name:')
    if a_name == 'q':
        break
    print(make_album( s_name,a_name))

# def get_sum_n(n):
#     if n == 1:
#         return 1
#     return n + get_sum_n(n-1)
#
# print(get_sum_n(2))
# print(get_sum_n(3))