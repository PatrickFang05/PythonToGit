def maxnumber(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

print(maxnumber(5, 9, 9))
print(maxnumber(124, 155, 882))

