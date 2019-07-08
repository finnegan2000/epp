import sys

def count_bits(x):
  ones = 0
  while x > 0:
    ones += x&1
    x>>=1
  return ones

for i in range(1, len(sys.argv)):
  print(count_bits(int(sys.argv[i])))
