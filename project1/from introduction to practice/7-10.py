#-*-coding:utf-8-*-
# 梦想度假村

# responses will be stored in the form{name:place}
responses = {}
polling_active = True
while polling_active:
    name = input("What's your name?")
    response = input("If you could visit one place in the world, where would you go?")
    # store the response，匹配键值对！{name:place}
    responses[name] = response      # 键name 对应的值
    # print(responses[name]+'==============')
    repeat = input("Would you like to let another person to respond? (yes/ no)")
    if repeat == 'no' :
        polling_active = False

print("--- Poll Result ---")
for name, response in responses.items():
    print(name + ' ' + 'would like to go ' + response + '.')