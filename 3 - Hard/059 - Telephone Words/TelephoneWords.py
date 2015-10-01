## CodeEval
## Telephone Words

import sys
import itertools

telephone = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

f = open(sys.argv[1], 'r')

for num in f:

    num = num.strip()
    if num:
        num = [telephone[int(n)] for n in num]
        gen = itertools.product(*num)
        sys.stdout.write(''.join(gen.next()))
        for s in gen:
            sys.stdout.write(',' + ''.join(s))
        sys.stdout.write('\n')


f.close()
