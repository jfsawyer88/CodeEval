## CodeEval
## Stepwise Word

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = line.split(' ')
        longest = ''
        for word in line:
            if len(longest) < len(word):
                longest = word

        sys.stdout.write(longest[0])
        for i in xrange(1, len(longest)):
            sys.stdout.write(' ' + '*'*i + longest[i])
        sys.stdout.write('\n')


f.close()
