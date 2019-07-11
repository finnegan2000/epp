def count_bits(x):
  ones = 0
  while x > 0:
    ones += x&1
    x>>=1
  return ones

def compute_parity(x):
  return count_bits(x) % 2

def compute_parity_2(x):
    result = 0
    while x > 0:
        result ^= 1
        x &= (x-1)
    return result

def compute_parity_3(x):
    #idea is to compute table of size eg 16 and cache it. This shows for size 2
    lookup = {0b0:0, 0b10:1, 0b01:1, 0b11:0}
    result = 0
    while x> 0:
        result ^= lookup[x & 0b11]
        x>>= 2
    return result

def check_parity(words):
  current_parity = 0
  for word in words:
    current_parity += compute_parity_2(word)
    current_parity%= 2
  return current_parity

def right_propagate(x):
    return x | ((x & ~(x-1)) -1)

def modulo_two_power(x, n):
    return x & (2**(n) -1)

def is_power_two(x):
    return x & ~(x-1) == x
