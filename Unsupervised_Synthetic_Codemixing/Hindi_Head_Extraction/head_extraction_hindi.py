import sys
count = 0
w = 0
with open(sys.argv[1], 'r') as f:
    for line in f:
        if (line[0] == ")"):
            continue
        elif (line[0] == "<" and line[1] == "/" and line[2] == "S"):
            print("#")
        else:
            line1 = line.split(' ')
            if (line1[0] == "<Sentence"):
                count = count + 1
                print("Sentence_id=%d" % (count))
            elif (line1[1] == "(("):
                head = line1[2]
                head = head.strip()
                if (len(line1) < 4):
                    print("H\t" + head + "\t" + "NULL")
                else:
                    inter1 = line1[4].split(',')
                    inter2 = inter1[0].split('\'')
                    word = inter2[1]
                    print("H\t" + head + "\t" + word)
            else:
                print("T\t" + line1[2].split('<')[0] + "\t" + line1[1])
