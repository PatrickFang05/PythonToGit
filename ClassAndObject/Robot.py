class Robot:
    count = 0
    def __init__(self, name):
        self.name = name
        Robot.count += 1
        print(f'{name} has been created')
    def sayHi(self):
        print(f'Hi! My name is {self.name}!')
    def die(self):
        Robot.count -= 1
        print(f'Destroying {self.name}')
    @classmethod
    def howMany(cls):
        if Robot.count > 1:
            s = 's'
            are = 'are'
        if Robot.count <= 1:
            s = ''
            are = 'is'
        print(f'There {are} {cls.count} robot{s} in my universe')

robot1 = Robot('R2D2')
robot2 = Robot('Moonwalker')
robot3 = Robot('Nebula')
robot4 = Robot('C3PO')
robot5 = Robot('Bob')
Robot.howMany()
robot1.sayHi()
robot5.sayHi()
robot1.die()
robot2.die()
robot5.die()
robot1.howMany()
