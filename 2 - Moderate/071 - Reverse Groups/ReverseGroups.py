## CodeEval
## Reverse Groups

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = line.split(';')
        seq = line[0].split(',')
        n = int(line[1])

        i = 0
        new = []
        while i < len(seq):
            # "then the remaining items in the end should be left as is"
            if i+n <= len(seq):
                new = new + [m for m in reversed(seq[i:i+n])]
            else:
                new = new + seq[i:]
            i += n

        sys.stdout.write(new[0])
        for s in new[1:]:
            sys.stdout.write(',' + s)
        sys.stdout.write('\n')


f.close()
