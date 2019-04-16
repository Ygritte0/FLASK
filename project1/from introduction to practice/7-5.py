#-*-coding:utf-8-*-
print("Please tell me how old are you ?")
age = int(input("Your age:"))
if age < 3:
    print("You will get a free ticket for the movie.")
    # break
elif age < 13:
    print("You will pay 10 dollars for your movie ticket.")
    # break
else:
    print("You will pay 15 dollars for your movie ticket.")
    # break