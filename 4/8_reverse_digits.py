import sys

def reverse_digits(x):
    sign = 1
    if x < 0:
        sign = -1
    x = abs(x)
    reversed = 0
    while x > 0:
        reversed, x = reversed * 10 + (x%10), x // 10
    return reversed * sign

print(reverse_digits(int(sys.argv[1])))
