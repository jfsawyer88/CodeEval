## CodeEval
## Hidden Digits

import sys

nums = {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4',
        '5':'5', '6':'6', '7':'7', '8':'8', '9':'9',
        'a':'0', 'b':'1', 'c':'2', 'd':'3', 'e':'4',
        'f':'5', 'g':'6', 'h':'7', 'i':'8', 'j':'9'}

f = open(sys.argv[1], 'r')

for line in f:

    printed = False
    for s in line:
        if s in nums:
            sys.stdout.write(nums[s])
            printed = True
    if printed == False:
        sys.stdout.write('NONE')
    sys.stdout.write('\n')


f.close()
