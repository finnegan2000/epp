from random import randint

def rng(a,b):
    rang = b - a + 1

    while True:
        number, bit = 0, 1

        while (bit >> 1) < rang:
            number |= bit * randint(0,1)
            bit <<= 1
        if number < rang:
            break
    return number + a

print(rng(1352132153,1347821394366769867896))
