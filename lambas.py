result = map(lambda x: x**2, [1, 2, 4, 99])
print(list(result))

lst = [1, 2, 3, 4, 5]

for x in lst:
    print(x, type(x))

lst = map(str, lst)

for x in lst:
    print(x, type(x))
