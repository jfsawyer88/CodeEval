## CodeEval
## String and Arrows

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        cnt = 0
        for i in xrange(len(line)-5+1):
            if line[i:i+5] == '>>-->' or line[i:i+5] == '<--<<':
                cnt += 1
        sys.stdout.write(str(cnt) + '\n')


f.close()
