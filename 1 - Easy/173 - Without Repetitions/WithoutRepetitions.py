## CodeEval
## Without Repetitions

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = line.split(' ')
        out = []
        for word in line:
            if word:
                cur = word[0]
                for s in word[1:]:
                    if s != cur[-1]:
                        cur = cur + s
                out.append(cur)
        sys.stdout.write(' '.join(out) + '\n')


f.close()
