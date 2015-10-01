## CodeEval
## Morse Code

import sys

morse = { '.-'   :'A', '-...' :'B', '-.-.' :'C', '-..'  :'D', '.'    :'E',
          '..-.' :'F', '--.'  :'G', '....' :'H', '..'   :'I', '.---' :'J',
          '-.-'  :'K', '.-..' :'L', '--'   :'M', '-.'   :'N', '---'  :'O',
          '.--.' :'P', '--.-' :'Q', '.-.'  :'R', '...'  :'S', '-'    :'T',
          '..-'  :'U', '...-' :'V', '.--'  :'W', '-..-' :'X', '-.--' :'Y',
          '--..' :'Z', '.----':'1', '..---':'2', '...--':'3', '....-':'4',
          '.....':'5', '-....':'6', '--...':'7', '---..':'8', '----.':'9',
          '-----':'0' }

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip().split('  ')
    for letter in line[0].split(' '):
        sys.stdout.write(morse[letter])
    for word in line[1:]:
        sys.stdout.write(' ')
        for letter in word.split(' '):
            sys.stdout.write(morse[letter])
    sys.stdout.write('\n')


f.close()
