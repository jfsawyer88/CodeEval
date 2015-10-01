## CodeEval
## Compare Points

import sys

def sign(a):
    return (a>0) - (a<0)

directions = ['SW',    'W', 'NW',
               'S', 'here',  'N',
              'SE',    'E', 'NE']

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        O, P, Q, R = [int(n) for n in line.split(' ')]
        sys.stdout.write(directions[(sign(Q-O)+1)*3 + (sign(R-P)+1)] + '\n')
        


f.close()
