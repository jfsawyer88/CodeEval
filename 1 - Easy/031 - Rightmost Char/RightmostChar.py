## CodeEval
## Rightmost Char

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:

    test = test.split(',')
    S = test[0]
    t = test[1][0]
    s_len = len(S)

    i = 1
    while i <= s_len:
        if t == S[s_len - i]:
            break
        i += 1
    sys.stdout.write(str(s_len - i) + "\n")


test_cases.close()
