## CodeEval
## Jolly Jumpers

import sys

f = open(sys.argv[1], 'r')

for seq in f:

    seq = seq.strip()
    if seq:
        seq = seq.split(' ')
        seq_len = int(seq[0])
        seq = [int(s) for s in seq[1:]]
        jumps = set(range(1, seq_len))

        for i in xrange(1, seq_len):
            jump = abs(seq[i] - seq[i-1])
            if jump in jumps:
                jumps.remove(jump)
            else:
                break

        if jumps:
            sys.stdout.write('Not jolly\n')
        else:
            sys.stdout.write('Jolly\n')


f.close()
