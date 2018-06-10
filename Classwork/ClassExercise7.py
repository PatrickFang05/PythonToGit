def drawTriangle(n):
    numLoops = n // 2 + 1
    for i in range(0, numLoops + 1):
        print(' ' * (numLoops - i) + ('#' * i))
drawTriangle(8)
