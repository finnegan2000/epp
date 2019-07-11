import sys, math

def reverse_digits(x):
    sign = 1
    if x < 0:
        sign = -1
    x = abs(x)
    reversed = 0
    while x > 0:
        reversed, x = reversed * 10 + (x%10), x // 10
    return reversed * sign

def is_palindrome(x):
    return  x >=0 and x == reverse_digits(x)

def is_palindrome_2(x):
    if x < 0:
        return False
    num_digits = math.floor(math.log10(x)) + 1

    while x >= 10:
        if x % 10 != x // (10 **(num_digits -1)):
            return False
        x= (x - (x // (10 **(num_digits -1))) * 10 **(num_digits -1))//10
        num_digits -= 2

    return True


print(is_palindrome_2(int(sys.argv[1])))
