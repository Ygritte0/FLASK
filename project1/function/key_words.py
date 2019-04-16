def get_name(**kwargs):
    if kwargs.get('name'):
        return 'name is %s' % kwargs.get('name')

def get_age(**kwargs):
    if kwargs.get('age'):
        return 'age is %s' % kwargs.get('age')

def get_gender(**kwargs):
    if kwargs.get('gender'):
        return 'gender is %s' % kwargs.get('gender')

def get_sth(**args):
    for func in [get_age, get_gender, get_name]:
        result = func(**args)
        if result:
            return result


get_sth(name='zm')
get_sth(gender='female')