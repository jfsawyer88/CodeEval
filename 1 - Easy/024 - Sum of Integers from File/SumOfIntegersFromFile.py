## CodeEval
## Sum of Integers from File

import sys

test_cases = open(sys.argv[1], 'r')

res = 0
for test in test_cases:
    res += int(test)

sys.stdout.write(str(res))
sys.stdout.write("\n")

test_cases.close()
