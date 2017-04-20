# because I imported classes_test in the python interpreter it created
# a new .pyc file

class Polygon:
    def __init__(self, no_of_sides):
        # self.n is an integer of the number of sides
        self.n = no_of_sides
        # self.sides is a list that sets each side to 0
        self.sides = [0 for i in range(no_of_sides)]

    # inputSides sets the sides to a user input of each side
    def inputSides(self):
        # sets each side to a float, using a for loop to go through each side
        self.sides = [float(raw_input("Enter side " + str(i+1) + " : ")) for i in range(self.n)]

    # displays the value of each side
    def dispSides(self):
        # for loop to display each side in the range of self.n
        for i in range(self.n):
            # prints the side number and its value
            print "Side", i + 1, "is", self.sides[i]

# this is a child class of Polygon
class Triangle(Polygon):
    # __init__ initializes Triangle as a subclass of Polygon, assigning 3 as the no_of_sides
    def __init__(self):
        Polygon.__init__(self, 3)

    # findArea creates a new function that calculates the area of a Triangle
    # class Triangle inherits the functions of class Polygon
    def findArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print "The area of the triangle is %0.2f" % area

# set t to class Triangle
t = Triangle()

# use function inputSides which comes from the parent class Polygon
t.inputSides()

# use function dispSides which comes from parent class Polygon
t.dispSides()

# use function findArea which comes from class Triangle
t.findArea()
