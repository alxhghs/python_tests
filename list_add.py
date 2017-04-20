a = []

a.insert(0, 'test')
a.append('this')
a.append('is')
a.insert(1, 'yup')
a.extend(['how', 'many', 'things'])

print a

print 'this will remove "%s".' % a.pop(-1)

print a
