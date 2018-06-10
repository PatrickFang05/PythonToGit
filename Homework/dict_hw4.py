def createSquares(n):
    dictionary = {}
    for i in range(1, n + 1):
        dictionary[i] = i * i
    print(dictionary)
createSquares(8)
