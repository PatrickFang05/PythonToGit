class Games:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.year = kwargs['year']
        self.genre = kwargs['genre']

Fortnite = Games(name='Fortnite', year='July 25, 2017', genre='Action + Adventure')
Minecraft = Games(name='Minecraft', year='May 17, 2009', genre='Sandbox + Survival')

class Fortnite(Games):
    def __init__(self, **kwargs):
        self.type = kwargs['type']
        self.cost = kwargs['cost']
        self.player = kwargs['player']
        super().__init__(**kwargs)
SaveTheWorld = Fortnite(type='Save the World', cost='$39.99', player='multiplayer')
BattleRoyale = Fortnite(type='Battle Royale', cost='Free', player='multiplayer')

class Minecraft(Games):
    def __init__(self, **kwargs):
        self.type = kwargs['type']
        self.player = kwargs['player']
        self.difficulty = kwargs['difficulty']
        super().__init__(**kwargs)
Survival = Minecraft(type='Survival', player='multiplayer', difficulty='hard')
Creative = Minecraft(type='Creative', player='multiplayer', difficulty='easy')
