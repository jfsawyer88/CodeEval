## CodeEval
## Mixed Content

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    ints = ''
    strs = ''

    for w in line.split(','):
        try:
            int(w)
            ints = ints + w + ','
        except:
            strs = strs + w + ','

    if 0 == len(strs)*len(ints):
        sys.stdout.write(line + "\n")
    else:
        sys.stdout.write(strs[:-1] + '|' + ints[:-1] + "\n")


f.close()
