## CodeEval
## Shortest Repetition

import sys

f = open(sys.argv[1], 'r')

for string in f:

    string = string.strip()
    str_len = len(string)
    first = string[0]
    shortest = first
    
    for i in xrange(1, str_len):
        if first == string[i]:
            if string == shortest * (str_len/len(shortest)):
                break
        shortest = shortest + string[i]

    sys.stdout.write(str(len(shortest)) + "\n")


f.close()
