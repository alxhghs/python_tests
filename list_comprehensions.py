x = int(input("Input x dimension: ")) # dimensions
y = int(input("Input y dimension: "))
z = int(input("Input z dimension: "))
n = int(input("Input max sum: ")) # max sum for x + y + z

print([ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])
