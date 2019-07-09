import sys

def closest_weight(x):
    lsb = x & ~(x-1)
    if lsb == 1:
        lsz = (x+1 & ~x)
        x |= lsz
        x ^= lsz >> 1
    else:
        x &= (x-1)
        x|= lsb >> 1
    return x
print(closest_weight(int(sys.argv[1])))
