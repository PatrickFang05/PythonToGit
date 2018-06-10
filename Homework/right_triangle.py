def drawTriangleRight(n):
    for i in range(1, n + 1):
        b = n - i
        line = ' ' * b + '#' * i
        print(line)

drawTriangleRight(13)
