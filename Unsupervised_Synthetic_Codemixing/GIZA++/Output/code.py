# Finds pairs that match in both the output files of GIZA++

import sys
with open(sys.argv[1], 'r') as f:
    for line in f:
        line1 = line.split(' ')
        engword = line1[0]
        hinword = line1[1]
        # print(engword,hinword,"1")
        with open(sys.argv[2], 'r') as f2:
            for lines in f2:
                line2 = lines.split(' ')
                engword2 = line2[1]
                hinword2 = line2[0]
                # print(engword2,hinword2,"2")
                if ((engword2 == engword) and (hinword2 == hinword)):
                    print(engword, hinword)
