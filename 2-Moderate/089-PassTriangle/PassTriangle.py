## CodeEval
## Pass Triangle

import sys

f = open(sys.argv[1], 'r')

array = []
for line in f:
    array.append([int(n) for n in line.strip().split(' ')])

while 1 < len(array):
    array = array[:-2] + [[array[-2][i] + max(array[-1][i], array[-1][i+1]) for i in xrange(len(array[-2]))]]

sys.stdout.write(str(array[0][0]) + '\n')

f.close()
