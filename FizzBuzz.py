class Solution(object):
    def fizzBuzz(self, n):
        self.n = n
        fizzBuzzList = []
        count = 1
        while count <= self.n:
            if count % 3 == 0 and count % 5 != 0:
                fizzBuzzList.append("Fizz")
            elif count % 3 != 0 and count % 5 == 0:
                fizzBuzzList.append("Buzz")
            elif count % 3 == 0 and count % 5 == 0:
                fizzBuzzList.append("FizzBuzz")
            else:
                fizzBuzzList.append(str(count))
            count += 1
        return fizzBuzzList

fizzBuzzObject = Solution()
print(fizzBuzzObject.fizzBuzz(15))
