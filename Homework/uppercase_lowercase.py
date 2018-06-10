def countCase(str):
    uppercase = 0
    lowercase = 0
    for c in str:
        if c.islower():
            lowercase += 1
        elif c.isupper():
            uppercase += 1
    print('lowercase =', lowercase)
    print('uppercase =', uppercase)

countCase('hisd1 SWe')
