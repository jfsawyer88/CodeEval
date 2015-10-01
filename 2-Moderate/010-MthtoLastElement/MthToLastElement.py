## CodeEval
## Mth to Last Element

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip().split(' ')
    n = int(line[-1])
    line = line[:-1]
    try:
        sys.stdout.write(line[-n] + '\n')
    except:
        pass


f.close()
