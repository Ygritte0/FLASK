#-*-coding:utf-8-*-
# 判断一个字符串是否为全字母句子,即包含字母a-z，每个字母至少出现一次
# def pangram(string):  # 读题错误
#     for x in string:
#         if x == " ":
#             return "This string is a pangram."
#
# print(pangram("line bottom"))

import string, sys
def ispangram(str1,alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphabet <= set(str1.lower())

print( ispangram('The quick brown fox jumps over the lazy dog.'))