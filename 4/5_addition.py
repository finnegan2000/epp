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
    pass


print(mult(int(sys.argv[1]),int(sys.argv[2])))
print(add(~8, 1))
