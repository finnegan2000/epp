def even_odd(X):
    even_p = 0
    odd_p = len(X) - 1
    while True:
        while not X[even_p] % 2 and even_p <= odd_p:
            even_p += 1
        while X[odd_p] % 2 and odd_p >=0:
            odd_p -= 1
        if even_p >= odd_p:
            break
        X[even_p], X[odd_p] = X[odd_p], X[even_p]
    return X

print(even_odd([1,3,5, 6]))
