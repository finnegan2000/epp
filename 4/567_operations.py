import sys

def add(a,b):
    mask = 1
    temp_a, temp_b = a, b
    total, carry = 0,0

    while temp_a !=0 or temp_b != 0 or carry != 0:
        a_bit, b_bit = a & mask, b & mask
        result = a_bit ^ b_bit ^ carry
        carry = (carry & a_bit & b_bit) | ((carry | a_bit | b_bit) & ~(carry ^ a_bit ^ b_bit))
        total |= result
        mask <<= 1
        carry <<= 1
        temp_a >>= 1
        temp_b >>= 1
    return total

def mult(x,y):

    counter = 0
    total = 0
    while y != 0:
        if y&1:
            total = add(total, x << counter)
        y>>= 1
        counter = add(counter, 1)

    return total

def divide(x,y):
    result, power = 0, 64
    y_power = y << power
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1
        result += 1 << power
        x -= y_power
    return result

def exp(x,y):
    lookup = {1:x}
    i = 2
    prev = x
    while i < y:
        lookup[i] = prev * prev
        prev = lookup[i]
        i <<= 1

    total = 1
    while y > 0:
        total *= lookup[y & ~(y-1)]
        y&= y-1
    return total

def exp_2(x,y):
    result, power = 1.0, y
    while power:
        if power & 1:
            result *= x
        x, power = x*x, power >> 1
    return result


print(exp_2(int(sys.argv[1]),int(sys.argv[2])))
