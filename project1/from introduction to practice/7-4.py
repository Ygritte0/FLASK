#-*-coding:utf-8-*-
pizza_elements = ''
while True:
    print("Please tell the elements of a pizza.")
    print("(Enter 'q' at any time to quit.)")
    p_elements = input("pizza_elements:")
    if p_elements == 'q':
        break
    print("We would like to add " +  ' ' + p_elements + ' '" to our pizza.")