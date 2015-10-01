## CodeEval
## Self Describing Numbers

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


test_cases = open(sys.argv[1], 'r')

for n in test_cases:

    n = int(n)
    num_digits = len(str(n))
    n_digits = digits(n)

    match = True
    n_dict = {i:0 for i in xrange(num_digits)}

    i = 0
    for i in xrange(num_digits):
        if n_digits[i] in n_dict:
            n_dict[n_digits[i]] = 1 + n_dict[n_digits[i]]
        else:
            break
        i += 1

    if match:
        for i in xrange(num_digits):
            if n_digits[i] != n_dict[i]:
                match = False

    if match:
        sys.stdout.write('1\n')
    else:
        sys.stdout.write('0\n')

test_cases.close()
