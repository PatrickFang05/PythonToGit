class Animal:
    def __init__(self, name, weight, sound):
        self.name = name
        self.weight = weight
        self.sound = sound
    def compareWeight(self, anotherAnimal):
        if self.weight > cat.weight:
            return self.name + 's ' + 'are heavier than ' + cat.name + 's'
        elif self.weight == cat.weight:
            return self.name + 's ' + 'are as heavy as ' + cat.name + 's'
        else:
            return self.name + 's ' + 'are lighter than ' + cat.name + 's'

dog = Animal('dog', 55, 'bark')
cat = Animal('cat', 30, 'meow')
horse = Animal('horse', 150, 'neigh')
print(dog.compareWeight(cat))


