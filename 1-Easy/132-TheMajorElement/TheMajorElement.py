## CodeEval
## The Major Element

import sys

f = open(sys.argv[1], 'r')

for seq in f:

    seq = [n for n in seq.strip().split(',')]
    cnt = {seq[0]:1}
    max_el = seq[0]
    for n in seq[1:]:
        if n in cnt:
            cnt[n] += 1
            if cnt[max_el] < cnt[n]:
                max_el = n
        else:
            cnt[n]  = 1
    if len(seq)//2 < cnt[max_el]:
        sys.stdout.write(n + '\n')
    else:
        sys.stdout.write('None\n')

f.close()
