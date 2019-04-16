#-*-coding:utf-8-*-
def formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + last_name + ' ' + middle_name
    else:
        full_name = first_name + ' ' + last_name
    return formatted_name.title()

# print(formatted_name('andy','green'))
while True:
    print('Please enter your name:')
    print("(Enter 'q' at any time to quit.)")
    f_name = input('first_name:')
    # print('asss:%s'% f_name)
    if f_name =='q':
        break
    l_name = input('last_name:')
    if l_name == 'q':
        break
    m_name = input('middle_name:')
    if m_name == 'q':
        break

    print('Hello,'+' '+ formatted_name(f_name,l_name,m_name) +'!')

    # formatted_name('jucy','green','lee')