class Movie:
    ratings = {'G': 'kids', 'PG13': 'teenagers', 'R': 'adults'}


    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.year = kwargs['year']
        self.genre = kwargs['genre']
        self.rating = kwargs['rating']
    def goodForKids(self):
        if self.rating == 'PG-13' or 'G':
            outcome = 'The movie ' + self.title + ' is good for teens'
        else:
            outcome = 'The movie' + self.title + ' is not good for teens'
        return outcome
    def __str__(self):
#        return 'The movie ' + self.title + ' is for ' + self.ratings[self.rating]
        return f'The movie {self.title} is a {self.ratings[self.rating]} movie'
fantastic_beasts = Movie(title='Fantastic Beasts', year=2016, genre='Fantasy', rating='PG13')
black_panther = Movie(title='Black Panther', year=2018, genre='Fantasy', rating='PG13')
minions = Movie(title='Minions', year=2015, genre='Adventure', rating='PG13')
print(black_panther.goodForKids())
print(black_panther.__str__())
