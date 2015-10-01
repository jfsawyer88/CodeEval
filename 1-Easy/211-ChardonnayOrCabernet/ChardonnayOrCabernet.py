## CodeEval
## Chardonnay or Cabernet

import sys

if 1 != len(sys.argv):
    f = open(sys.argv[1], 'r')
else:
    import os
    f = open(os.getcwd() +  '/test.txt')


for line in f:

    line = line.strip()
    if line:
        wines, letters = line.split(' | ')
        wines = wines.split(' ')
        letters_count = dict()
        for l in letters:
            if l in letters_count:
                letters_count[l] += 1
            else:
                letters_count[l] = 1

        out = []
        for wine in wines:
            keep = True
            for l in letters_count:
                keep = keep and letters_count[l] <= wine.count(l)
            if keep:
                out.append(wine)
            
        if out:
            sys.stdout.write(' '.join(out) + '\n')
        else:
            print 'False\n'


f.close()
