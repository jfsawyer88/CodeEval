## CodeEval
## Delta Time

import sys

def digits(n, b=10):
    "outputs the digits of n in base b"
    res = []
    while 0 < n:
        d = n % b
        n = (n - d)/b
        res.append(d)
    res.reverse()
    return res

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        
        line = line.split(' ')
        
        t0 = [int(n) for n in line[0].split(':')]
        t1 = [int(n) for n in line[1].split(':')]
        
        t0 = sum([t0[i]*60**(2-i) for i in xrange(3)])
        t1 = sum([t1[i]*60**(2-i) for i in xrange(3)])

        out = digits(abs(t1-t0), 60)
        out = (3 - len(out))*[0] + out
        out = [str(n) for n in out]
        out = ['0'*(2-len(s)) + s for s in out]
        sys.stdout.write(':'.join(out) + '\n')


f.close()
