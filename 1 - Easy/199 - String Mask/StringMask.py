## CodeEval
## String Mask

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = line.split(' ')
        word = line[0]
        mask = line[1]
        for i in xrange(len(mask)):
            if '1' == mask[i]:
                sys.stdout.write(word[i].upper())
            else:
                sys.stdout.write(word[i])
        sys.stdout.write('\n')


f.close()

