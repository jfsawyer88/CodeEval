## CodeEval
## Split the Number

import sys

alpha = 'abcdefghijklmnopqrstuvwxyz'

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip().split(' ')
    N = line[0]
    pat = line[1]
    if '-' in pat:
        pat = pat.split('-')
        a = sum([int(N[alpha.find(pat[0][i])]) * (10**(len(pat[0])-i-1)) for i in xrange(len(pat[0]))])
        b = sum([int(N[alpha.find(pat[1][i])]) * (10**(len(pat[1])-i-1)) for i in xrange(len(pat[1]))])
        sys.stdout.write(str(a-b) + '\n')
    if '+' in pat:
        pat = pat.split('+')
        a = sum([int(N[alpha.find(pat[0][i])]) * (10**(len(pat[0])-i-1)) for i in xrange(len(pat[0]))])
        b = sum([int(N[alpha.find(pat[1][i])]) * (10**(len(pat[1])-i-1)) for i in xrange(len(pat[1]))])
        sys.stdout.write(str(a+b) + '\n')

f.close()
