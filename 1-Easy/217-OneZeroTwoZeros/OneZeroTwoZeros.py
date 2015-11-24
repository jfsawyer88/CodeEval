## CodeEval
## One Zero, Two Zeros...

import sys

test_cases = open(sys.argv[1], 'r')

def count(v, a):
    """counts all the occurences of a in list v"""
    cnt = 0
    for n in v:
        if a == n:
            cnt += 1
    return cnt
    

a = [[0]]
vec = [0]
i = 1
while i < 10:
    a.append([n+1 for n in a[-1]] + a[-1])
    vec = vec + a[-1]
    i += 1

for test in test_cases:
    a, b = map(int, test.split(' '))
    sys.stdout.write(str(count(vec[:b], a)) + '\n')


test_cases.close()
