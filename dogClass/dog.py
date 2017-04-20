class Dog(object):
    """A generic dog object."""
    def __init__(self, name, breed):
        self.name = name.title()
        self.breed = breed.title()

    def roll_over(self):
        print "%s rolled over!" % self.name

    def sit(self):
        print "%s sat down." % self.name

    def print_breed(self):
        print "%s is a %s." % (self.name, self.breed)
