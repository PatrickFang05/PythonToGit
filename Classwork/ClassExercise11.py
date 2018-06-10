class Animal:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.weight = kwargs['weight']
        self.sound = kwargs['sound']
    def __str__(self):
        return f'{self.name} is an animal'

dog = Animal(name='dog', weight=55, sound='bark')
cat = Animal(name='cat', weight=30, sound='meow')

class Cat(Animal):
    def __init__(self, **kwargs):
        self.breed = kwargs['breed']
        super().__init__(**kwargs)
    def __str__(self):
        return f'{self.name} is a {self.breed} cat'
cat1 = Cat(name='tom', weight='7', sound='meow', breed='Persian')
cat2 = Cat(name='jerry', weight='3', sound='meow', breed='Russian Blue')
cat3 = Animal(name='jerry', weight='3', sound='meow', breed='Russian Blue')
print(cat1)
print(cat2)
print(cat3)

class Dog(Animal):
    def __init__(self, **kwargs):
        self.breed = kwargs['breed']
        super().__init__(**kwargs)
    def __str__(self):
        return f'{self.name} is a {self.breed} dog'
    def catDogDifferences(dog, cat):
        if dog.name != cat.name:
            return f'The names are different'
        else:
            return f'The names are the same'
        if dog.weight != cat.weight:
            return f'Their weights are different'
        else:
            return f'Their weights are equal'
        if dog.sound != cat.sound:
            return f'Their sounds are different'
        else:
            return f'Their sounds the same'
        if dog.breed != cat.breed:
            return f'Their breed is different'
        else:
            return f'Their breed is the same'
dog1 = Dog(name='Lulu', weight='55', sound='bark', breed='Labrodoodle')
dog2 = Dog(name='Caly', weight='50', sound='bark', breed='Goldendoodle')
dog3 = Animal(name='Caly', weight='50', sound='bark', breed='Goldendoodle')
print(dog.catDogDifferences(dog1, cat2))
