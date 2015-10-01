## CodeEval
## Hex to Decimal

import sys

digits = {'0': 0, '1': 1, '2': 2, '3': 3,
          '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, 'a':10, 'b':11,
          'c':12, 'd':13, 'e':14, 'f':15}

f = open(sys.argv[1], 'r')

for h in f:
    
    h = h.strip()
    num_h_digits = len(h)
    sys.stdout.write(str(sum([digits[h[i]] * 16 ** (num_h_digits - (i+1)) for i in xrange(num_h_digits)])) + "\n")
    

f.close()
