## CodeEval
## Email Validation

import sys
import re

pat = re.compile('^[a-zA-Z0-9._+%\-$]*\@[a-zA-Z0-9]*\.[a-z]{2,4}')

f = open(sys.argv[1], 'r')

for email in f:

    email = email.strip()
    match = pat.findall(email)
    if match:
        out = email == match[0]
    else:
        out = False

    sys.stdout.write(str(out).lower() + '\n')


f.close()
