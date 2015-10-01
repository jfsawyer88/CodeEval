## CodeEval
## Telephone Words

import sys

telephone = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

f = open(sys.argv[1], 'r')

for num in f:

    num = num.strip()
    if num:
        num = [telephone[int(n)] for n in num]
        out = ['']
        for digit in num:
            out = [x + y for x in out for y in digit]
        sys.stdout.write(','.join(out) + '\n')


f.close()
