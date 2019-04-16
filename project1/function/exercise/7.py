#-*-coding:utf-8-*-
# 计算大小写字母的个数
def string_test(s):
    d = {"UPPER _CASE":0, "LOWER_CASE":0}  # 用字典，键值对的形式分别定义大小写字母的个数，大写：个数；小写：个数
    for c in s:   # 遍历s中的每一个字母，
        if c.isupper():  # 如果该字母是大写的
            d["UPPER _CASE"] += 1 #大写字母的个数加一
        elif c.islower():# 如果该字母是小写的
            d["LOWER_CASE"] += 1  # 小写字母个数加一
        # else:
        #     pass
    print("Original String :", s)
    print("No.of Upper case characters :", d["UPPER _CASE"])
    print("No.of Lower case Characters :", d["LOWER_CASE"])

string_test("I am a Student.")# 计算大小写字母的个数
