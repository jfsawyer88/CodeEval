## CodeEval
## Compressed Seqeuence

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip().split(' ')
    seq = [line[0]]
    cnt = [1]

    for i in xrange(1, len(line)):
        if line[i] == line[i-1]:
            cnt[-1] += 1
        else:
            seq.append(line[i])
            cnt.append(1)

    sys.stdout.write(str(cnt[0]) + ' ' + seq[0])
    for i in xrange(1, len(cnt)):
        sys.stdout.write(' ' + str(cnt[i]) + ' ' + seq[i])
    sys.stdout.write('\n')


f.close()
