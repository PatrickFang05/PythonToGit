def findUnique(n):
    list = []
    for i in n:
        if i not in list:
            list.append(i)
    print(list)

findUnique([])
