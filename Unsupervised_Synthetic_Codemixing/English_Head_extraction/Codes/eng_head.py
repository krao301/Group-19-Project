import sys
count = 0
NP = ['NN', 'NNS', 'NNP', 'NNPS', 'PRP', 'PRP$']
VP = ['VB', 'VBD', 'VBN', 'VBG', 'VBP', 'VBG']

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        lines = line.split(' ')
        # print(lines[0])
        if (lines[0] == "(ROOT"):
            count = count + 1
            if (count != 1):
                print("#")
            print("Sentence_id=%d" % (count))

        elif (len(lines) < 2):
            continue

        elif (lines[0] == "(NP"):
            length = len(lines)
            flag = 0
            for x in range(length - 1, 0, -1):
                if (x % 2 == 0):
                    word = lines[x].split(')')[0]
                elif (x % 2 == 1):
                    tag = lines[x].split('(')[1]
                    for y in range(0, 6):
                        if (tag == NP[y]):
                            print("H\t" + "NP\t" + word)
                            flag = 1
                            break
                        elif (y == 5 and x == 1):
                            print("H\tNULL\tNULL")
                if (flag == 1):
                    break
            for x in range(1, length):
                if (x % 2 == 1):
                    tag = lines[x].split('(')[1]
                elif (x % 2 == 0):
                    word = lines[x].split(')')[0]
                    print("T\t" + tag + "\t" + word)

        elif (lines[0] == "(VP"):
            length = len(lines)
            flag = 0
            for x in range(length - 1, 0, -1):
                if (x % 2 == 0):
                    word = lines[x].split(')')[0]
                elif (x % 2 == 1):
                    tag = lines[x].split('(')[1]
                    for y in range(0, 6):
                        if (tag == VP[y]):
                            print("H\t" + "VP\t" + word)
                            flag = 1
                            break
                        elif (y == 5 and x == 1):
                            print("H\tNULL\tNULL")
                if (flag == 1):
                    break
            for x in range(1, length):
                if (x % 2 == 1):
                    tag = lines[x].split('(')[1]
                elif (x % 2 == 0):
                    word = lines[x].split(')')[0]
                    print("T\t" + tag + "\t" + word)

        else:
            length = len(lines)
            if (length % 2 == 0):
                if len(lines[0]) == 2:
                    print("H\tNULL\tNULL")
                    print("T\tSYM\t" + lines[1].split(")")[0])
                else:
                    # length = len(lines)
                    flag = 0
                    for x in range(length - 1, -1, -1):
                        if (x % 2 == 1):
                            word = lines[x].split(')')[0]
                        elif (x % 2 == 0):
                            tag = lines[x].split('(')[1]
                            for y in range(0, 6):
                                if (tag == NP[y]):
                                    # print(y)
                                    print("H\t" + "NP\t" + word)
                                    flag = 1
                                    break
                        if (flag == 1):
                            break

                    if flag == 0:
                        for x in range(length - 1, -1, -1):
                            if (x % 2 == 1):
                                word = lines[x].split(')')[0]

                            elif (x % 2 == 0):
                                tag = lines[x].split('(')[1]
                                for y in range(0, 6):
                                    if (tag == VP[y]):
                                        print("H\t" + "VP\t" + word)
                                        flag = 1
                                        break
                                    elif (y == 5 and x == 0):
                                        print("H\tNULL\tNULL")

                            if (flag == 1):
                                break

                    for x in range(0, length):
                        if (x % 2 == 0):
                            tag = lines[x].split('(')[1]
                        elif (x % 2 == 1):
                            word = lines[x].split(')')[0]
                            print("T\t" + tag + "\t" + word)

            else:
                print("H\tNULL\tNULL")

                for x in range(1, length):
                    if (x % 2 == 1):
                        tag = lines[x].split('(')[1]
                    elif (x % 2 == 0):
                        word = lines[x].split(')')[0]
                        print("T\t" + tag + "\t" + word)


print("#\n")
