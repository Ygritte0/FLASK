#-*-coding:utf-8-*-
def make_album(siger_name, album_name,songs_count='10'):
    # info_of_album = 'The ' + ' ' + album_name + "'s" + ' ' + 'author' +' ' + siger_name
    info_of_album = {'Author':siger_name, 'album':album_name,'how many songs':songs_count}
    return info_of_album

print(make_album('Talor Swift','Red'))
print(make_album('Talor Swift','22'))
print(make_album('Talor Swift','1989',9))