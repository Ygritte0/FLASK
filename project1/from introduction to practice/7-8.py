#-*-coding:utf-8-*-
sandwich_orders = ['beef ','vegetarian','fish','chicken breast','tuna']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()  # 一个一个删
    print("I'm working on your" + current_sandwich + "sandwich")
    finished_sandwiches.append(current_sandwich)  # 一个一个加

print('\n')
for x in finished_sandwiches:
    print("I made your " + ' ' + x + ' '+ 'sandwich.')
