def isPrime(n):

    if n == 2:
        print(n, 'TRUE')
        return

    for i in range(2, n):
        if n % i == 0:
            print(i)

    for i in range(2, n):
        if n % i == 0:
            print(n, 'FALSE')
            return
    print(n, 'TRUE')

isPrime()
