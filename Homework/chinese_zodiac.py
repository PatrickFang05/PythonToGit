def getZodiac(year):
    b = max(2018, year)
    zodiac = b * ['Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster']
    a = int(year) - 2018
    print(zodiac[a])

getZodiac(2846)
