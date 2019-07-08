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
        result += 1
        x &= (x-1)
    return result

def check_parity(words):
  current_parity = 0
  for word in words:
    current_parity += compute_parity_2(word)
    current_parity%= 2
  return current_parity

print(check_parity([1,1, 7]))
