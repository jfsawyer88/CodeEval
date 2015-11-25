## CodeEval
## Valid Parenthesis

import sys


def valid_ex(ex):
    while ex:
        if ex[0] in ')]}':
            return False

        p = '([{'.index(ex[0])
        v = [0, 0, 0]
        v[p] += 1
        i = 1
        while (v[p] != 0) and i < len(ex):
            if ex[i] in '([{':
                v['([{'.index(ex[i])] += 1
            if ex[i] in ')]}':
                v[')]}'.index(ex[i])] -= 1
            i += 1
        if v == [0,0,0]:
            ex = ex[:(i-1)] + ex[i:]
            ex = ex[1:]
        else:
            return False
    return True


expressions = open(sys.argv[1], 'r')

for ex in expressions:
    sys.stdout.write(str(valid_ex(ex.strip())) + '\n')

expressions.close()
