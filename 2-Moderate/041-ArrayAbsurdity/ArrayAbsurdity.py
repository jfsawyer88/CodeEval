## CodeEval
## Array Absurdity

import sys

f = open(sys.argv[1], 'r')

for array in f:

    array = array.strip()
    if array:
        array = array.split(';')[1].split(',')
        seen = set()
        for n in array:
            if n in seen:
                sys.stdout.write(n + '\n')
                break
            else:
                seen.add(n)


f.close()
