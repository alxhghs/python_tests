from dog import Dog

class Chihuahua(Dog):
    """Chihuahua object"""
    def __init__(self, name, breed, size):
        super(Chihuahua, self).__init__(name, breed)
        self.size = size

    def chihuahua_size(self):
        print "The Chihuahua is a size %d." % self.size
