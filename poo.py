class Sample(object):
    pass


x = Sample()
type(x)


class Dog(object):
    def __init__(self, raca):
        self.raca = raca


sam = Dog(raca='Pit')
sam.raca


class Cat(object):
    species = 'mamifero'

    def __init__(self, raca, weight):
        self.raca = raca
        self.weight = weight


tom = Cat(raca="Per", weight="5")
tom.weight
