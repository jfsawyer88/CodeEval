## CodeEval
## Json Menu IDs

import sys

roman = [['', 'M', 'MM', 'MMM'],
         ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
         ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
         ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']]

f = open(sys.argv[1], 'r')

for n in f:

    n = n.strip()
    digits = [0, 0, 0, 0]
    for i in xrange(1, 1+len(n)):
        digits[-i] = int(n[-i])

    for i in xrange(4):
        sys.stdout.write(roman[i][digits[i]])
    sys.stdout.write("\n")


f.close()
