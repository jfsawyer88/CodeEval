## CodeEval
## Sum of Primes

import sys
import math


def prime_pi(n):
    "count primes below n"
    r = int(n ** 0.5)
    V = [n//i for i in range(1,r+1)]
    V += list(range(V[-1]-1,0,-1))
    S = {i:i-1 for i in V}
    for p in range(2,r+1):
        if S[p] > S[p-1]:  # p is prime
            sp = S[p-1]  # sum of primes smaller than p
            p2 = p*p
            for v in V:
                if v < p2: break
                S[v] -= (S[v//p] - sp)
    return S[n]


def sum_of_primes_below(n):
    r = int(n**0.5)
    assert r*r <= n and (r+1)**2 > n
    V = [n//i for i in range(1,r+1)]
    V += list(range(V[-1]-1,0,-1))
    S = {i:i*(i+1)//2-1 for i in V}
    for p in range(2,r+1):
        if S[p] > S[p-1]:  # p is prime
            sp = S[p-1]  # sum of primes smaller than p
            p2 = p*p
            for v in V:
                if v < p2: break
                S[v] -= p*(S[v//p] - sp)
    return S[n]


n = 1000 # int(sys.argv[1])

def sum_of_first_primes(n):
    init = int(n * (math.log(n) + (math.log(math.log(n)) - 1) + (math.log(math.log(n))-2)/(math.log(n)) - (((math.log(math.log(n)))**2) - 6*math.log(math.log(n) + 11))/(2 * math.log(n)**2)))

    pp = prime_pi(init)
    while pp != n:
        
        i = 0
        while pp > n:
            pp = prime_pi(init - 2**i)
            i = i + 1
        init = init - 2**(i-1)

        i = 0
        while pp < n:
            pp = prime_pi(init + 2**i)
            i = i + 1
        init = init + 2**(i-1)

    return sum_of_primes_below(init)


sys.stdout.write(str(sum_of_first_primes(n)))
