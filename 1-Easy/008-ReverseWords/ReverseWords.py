## CodeEval
## Prime Palindrome

import sys

test_cases = open(sys.argv[1], 'r')

i = 0
for test in test_cases:

    if '' != test:
        words = test.split()
        j = len(words) - 1
        while True:
            sys.stdout.write(words[j])
            j = j - 1

            if j > -1:
                sys.stdout.write(" ")
            else:
                sys.stdout.write("\n")
                break

test_cases.close()
