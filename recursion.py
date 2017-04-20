def summation(a):
    if a <= 0:
        return 0
    else:
        return a + summation(a-1)

count = 10
while count > 0:
    print("Summation of", count, "=", summation(count))
    count -= 1
