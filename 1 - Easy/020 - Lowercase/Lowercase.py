## CodeEval
## Lowercase

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    sys.stdout.write(test.lower())

sys.stdout.write("\n")
test_cases.close()
