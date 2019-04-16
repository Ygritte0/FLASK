#-*-coding:utf-8-*-
# 回文词，即左右对称的单词、短语等
def palindrome(string1):
    left_pos = 0
    right_pos = len(string1) - 1
    while right_pos > left_pos:
        left_pos += 1
        right_pos -= 1
    if string1[left_pos] == string1[right_pos]:
        return True
    return False

print (palindrome('ada'))
