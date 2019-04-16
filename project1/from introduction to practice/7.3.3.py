#-*-coding:utf-8-*-
responses = {}
polling_active = True
while polling_active:
    name = input("What's your name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response   # ??? 键name 对应的值为response
    # print(responses[name])
    repeat = input("Would you like to let another person to respond? (yes/ no)")
    if repeat == 'no' :
        polling_active = False

print("--- Poll Result ---")
for name, response in responses.items():
    print(name + ' ' + 'would like to climb ' + response + '.')