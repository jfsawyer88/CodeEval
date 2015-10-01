## CodeEval
## Prime Numbers

import sys


def primesto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1) 
    for n in range(int(limit**0.5 + 1.5)):
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]


f = open(sys.argv[1], 'r')

for n in f:

    n = n.strip()
    if n:
        n = int(n)
        primes = primesto(n)
        if n == primes[-1]:
            primes = primes[:-1]
        sys.stdout.write(str(primes[0]))
        for i in xrange(1, len(primes)):
            sys.stdout.write(',' + str(primes[i]))
        sys.stdout.write('\n')


f.close()
