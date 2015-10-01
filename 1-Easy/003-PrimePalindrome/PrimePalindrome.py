## CodeEval
## Prime Palindrome

import sys

def is_power_of(n, p):
    while 1 < n:
        if 0 == n % p :
            n = n/p
        else:
            return False
    return True


def is_prime(n):
    "determines if the input is prime"
    if 0 == n % 2:
        return False
    i = 3
    while i < 1 + n ** 0.5:
        if 0 == n % i:
            return False
        i = i + 2
    return True


def reverse_digits(n):
    res = 0
    while 0 < n:
        d = n % 10
        n = (n - d) / 10
        res = res*10 + d
    return res
    

def largest_palprime_below_pow10(n):
    
    i = len(str(n)) - 1

    if i == 1:
        return 7
    elif i == 2:
        return 11

    if 0 == i % 2:
        i = i - 1

    j = (i+1) // 2
    while j > 1:
        for m in xrange(10**j - 1, 10**(j-1) - 1, -1):
            l = (10**j)*(m//10) + reverse_digits(m)
            if is_prime(l):
                return l
        j -= 1

    return 11


def largest_palindrome_below(n):

    if n == reverse_digits(n):
        return n
    
    num_digits = len(str(n))
    i = num_digits // 2
    j = num_digits - i
    first    = n // (10**j)
    first_p1 = n // (10**i) #first plus middle term
    last     = n  % (10**i)

    if reverse_digits(first) >= last:
        first_p1 = first_p1 - 1
        
    return first_p1 * 10**i + reverse_digits(first_p1 // 10**(j-i))


def largest_palprime_below(n):
    
    num_digits = len(str(n))
    
    if is_power_of(n, 10):
        if 1 == num_digits % 2:
            return largest_palprime_below_pow10(10 ** (num_digits - 1))
        return largest_palprime_below_pow10(n)
    elif 0 == num_digits % 2:
        return largest_palprime_below_pow10(10 ** (num_digits - 1))

    n = largest_palindrome_below(n)
    j = num_digits // 2
    for m in xrange(n // 10**j, 10**(j-1) - 1, -1):
        l = (10**(j+1))*(m//10) + reverse_digits(m)
        if is_prime(l):
            return l

    return largest_palprime_below_pow10(10**(num_digits-2))

n = 1000 #int(sys.argv[1])
sys.stdout.write(str(largest_palprime_below(n)))
