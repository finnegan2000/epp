def swap_bits(x, i, j):
    i_bit = x >> i & 1
    j_bit = x >> j & 1
    return x - (x& (1 <<i | 1 << j)) | (i_bit << j) | (j_bit << i)


def swap_bits_2(x,i,j):
    if x >> i & 1 != x >> j & 1:
        x^= 1<<j | 1<<i
    return x

print("{0:b}".format(swap_bits_2(0b01001001, 0, 2)))
