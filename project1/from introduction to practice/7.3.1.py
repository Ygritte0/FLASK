#-*-coding:utf-8-*-
# 在列表之间移动元素
unconfirmed_users = ['Alice','Arya','Sansa']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user:" + current_user.title())
    confirmed_users.append(current_user)
    # print(confirmed_users.title())
print("The following users have been confirmed:") # 所有用户都验证完毕后
for confirmed_user in confirmed_users:  # 都验证完毕后，为了逐一输出已验证的用户，循环
    print(confirmed_user.title())