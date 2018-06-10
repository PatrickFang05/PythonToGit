class Movie:
    ratings = {'G': 'kids', 'PG13': 'teenage', 'R': 'adult'}


    def __init__(self, title, year, genre, rating):
        self.title = title
        self.year = year
        self.genre = genre
        self.rating = rating
    def goodForKids(movie):
        if movie.rating == 'PG-13' or 'G':
            return "TRUE"
        else:
            return "FALSE"
fantastic_beasts = Movie('Fantastic Beasts', 2016, 'Fantasy', 'PG-13')
black_panther = Movie('Black Panther', 2018, 'Fantasy', 'PG-13')
minions = Movie('Minions', 2015, 'Adventure', 'PG-13')
print(black_panther.goodForKids())
