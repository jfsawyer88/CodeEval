## CodeEval
## Age Distribution

import sys

f = open(sys.argv[1], 'r')

for age in f:

    age = age.strip()
    if age:
        age = int(age)
        if   0 <= age and age <= 2:
            sys.stdout.write('Still in Mama\'s arms\n')
        elif 3 <= age and age <= 4:
            sys.stdout.write('Preschool Maniac\n')
        elif 5 <= age and age <= 11:
            sys.stdout.write('Elementary school\n')
        elif 12 <= age and age <= 14:
            sys.stdout.write('Middle school\n')
        elif 15 <= age and age <= 18:
            sys.stdout.write('High school\n')
        elif 19 <= age and age <= 22:
            sys.stdout.write('College\n')
        elif 23 <= age and age <= 65:
            sys.stdout.write('Working for the man\n')
        elif 66 <= age and age <= 100:
            sys.stdout.write('The Golden Years\n')
        else:
            sys.stdout.write('This program is for humans\n')


f.close()
