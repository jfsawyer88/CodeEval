## CodeEval
## Trick or Treat

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    v, z, w, h = [int(v.split(' ')[1]) for v in test.split(', ')]
    avg = ((3*v + 4*z + 5*w) * h) // (v + z + w)
    sys.stdout.write(str(avg) + '\n')

test_cases.close()
