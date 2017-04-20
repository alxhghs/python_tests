x = int(input("Enter number to fizzbuzz!: "))
for i in range(x):
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 5 == 0 and i % 3 != 0:
        print("Buzz")
    elif i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
