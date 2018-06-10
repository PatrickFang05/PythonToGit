#Take the following Python dictionary:
#  ages = { "Peter": 10, "Isabel": 11, "Anna": 9, "Thomas": 10, "Bob": 10,
#  "Joseph": 11, "Maria": 12, "Gabriel": 10, }
# 1. How many students are in the dictionary? Search for the "len" function.
# 2. Implement a function that receives the "ages" dictionary as parameter and return the average age
# of the students. Traverse all items on the dictionary using the "items" method as above.
# 3. Implement a function that receives the "ages" dictionary as parameter and returns
# the name of the oldest student.
# 4. Implement a function that receives the "ages" dictionary and a number "n" and returns a
# new dict where each student is n years older. For instance, new_ages(ages, 10) returns a copy of
# "ages" where each student is 10 years older.
ages = {"Peter": 10, "Isabel": 11, "Anna": 9, "Thomas": 10, "Bob": 10, "Joseph": 11, "Maria": 12, "Gabriel": 10, }
# Q1
print(len(ages))
# Q2
def averageAge(ages):
    a = ages.items()
    sum = 0
    for i in a:
        sum += i[1]
    b = len(ages)
    return sum / b
average = averageAge(ages)
print(average)
# Q3
def oldestAge(ages):
    a = ages.items()
    max = 0
    name = ""
    for i in a:
        if i[1] > max:
            max = i[1]
            name = i[0]
    return name
print(oldestAge(ages))
# Q4
def newAge(year):
    ages2 = {}
    a = ages.items()
    for i in a:
        ages2[i[0]] = i[1] + 10
    return ages2
print(newAge(ages))
