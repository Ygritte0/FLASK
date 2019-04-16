#-*-coding:utf-8-*-
print("I'm sorry,we're all out of pastrami today.")
sandwich_orders = ['beef ','pastrami','vegetarian','pastrami','fish','pastrami','chicken breast','tuna','pastrami']
finished_sandwiches =[]
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your" + current_sandwich +'sandwich')
    finished_sandwiches.append(current_sandwich)

print('\n')
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + "sandwich.")


