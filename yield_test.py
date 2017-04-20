g = (2**x for x in range(100))

def generator():
    for i in range(20):
        yield i*i

g = generator()
for i in g:
    print(i)
