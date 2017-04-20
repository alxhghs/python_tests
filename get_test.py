dict = {'name1': 'alex', 'name2': 'maggie', 'name3': 'chris'}

dict['name1']

a = dict.get('name3', None)
print a
b = dict.get('name7', None)
print b
c = dict.get('name10')
print c
