class Animal(object):
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def inputAnimal(self):
        self.size = raw_input("What is the size? ")
        self.color = raw_input("What is the color? ")

    def dispAnimal(self):
        print "The animal is %s." % self.size
        print "The animal is %s." % self.color

class Canine(Animal):
    def __init__(self, trick):
        Animal.__init__(self, "size", "color")
        self.trick = trick

    def trickInput(self):
        self.trick = raw_input("What is the canine's favorite trick? ")

    def dispTrick(self):
        print "The canine's favorite trick is %s." % self.trick

class Dog(Canine):
    def __init__(self, owner):
        Canine.__init__(self, "trick")
        self.owner = owner

    def dogOwner(self):
        self.owner = raw_input("Who owns the dog? ").title()

    def dispOwner(self):
        print "The dog's owner is %s." % self.owner


spot = Dog("owner")

spot.inputAnimal()

spot.dispAnimal()

spot.trickInput()

spot.dispTrick()

spot.dogOwner()

spot.dispOwner()
