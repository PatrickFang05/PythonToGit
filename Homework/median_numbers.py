def getMedian(x, y, z):
    if x <= y <= z or z <= y <= x:
        print(y)
    elif y <= z <= x or x <= z <= y:
        print(z)
    elif z <= x <= y or y <= x <= z:
        print(x)


print(getMedian())
