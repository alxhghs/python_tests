def outer(x):
    y = x * 2
    def inner(z):
        return y + z
    return inner

q = outer(2)
r = outer(3)

print q(2)
print q(1)

print r(2)
print r(1)
