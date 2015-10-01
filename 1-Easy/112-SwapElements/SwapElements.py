## CodeEval
## Swap Elements

import sys

def swap_elements(v, s):
    if s[0] == s[1]:
        return v
    else:
        v[s[0]] = v[s[0]] + v[s[1]]
        v[s[1]] = v[s[0]] - v[s[1]]
        v[s[0]] = v[s[0]] - v[s[1]]
        return v

f = open(sys.argv[1], 'r')

for line in f:
    
    line = line.split(' : ')
    vec = [int(n) for n in line[0].split()]
    swaps = line[1].split(', ')

    for swap in swaps:
        swap = [int(i) for i in swap.split('-')]
        vec = swap_elements(vec, swap)

    sys.stdout.write(str(vec[0]))
    for i in xrange(1, len(vec)):
        sys.stdout.write(' ' + str(vec[i]))
    sys.stdout.write("\n")

f.close()
