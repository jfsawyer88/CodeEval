## CodeEval
## Digit Statistics

import sys

loops = {2: [2, 4, 8, 6],
         3: [3, 9, 7, 1],
         4: [4, 6],
         5: [5],
         6: [6],
         7: [7, 9, 3, 1],
         8: [8, 4, 2, 6],
         9: [9,1]}

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = line.split(' ')
        a = int(line[0])
        n = int(line[1])

        loop = loops[a%10]
        nloops = n/len(loop)
        out = {i:0 for i in xrange(10)}
        for val in loop:
            out[val] = nloops
        for val in loop[:n%len(loop)]:
            out[val] += 1

        sys.stdout.write(', '.join([str(n) + ': ' + str(out[n]) for n in out]) + '\n')


f.close()
