import sys
eng = open(sys.argv[1], "r")
eng_list = eng.readlines()
eng.close()
hin = open(sys.argv[2], "r")
hin_list = hin.readlines()
hin.close()
giza = open(sys.argv[3], "r")
giza_list = giza.readlines()
giza.close()
i = 0
j = 0
while i < len(eng_list) and j < len(hin_list):
    # print(i,j)
    if (eng_list[i].split('_')[0] == "Sentence"):
        print(eng_list[i].strip())
        i = i + 1
        j = j + 1

        start = j
        start1 = i

        while eng_list[i].strip() != "#":
            # print(i,j)
            split_eng = eng_list[i].split('\t')
            if (split_eng[0] == "H" and (split_eng[1] == "NP" or split_eng[1] == "VP")):
                match = 0
                start_chunk = j
                while hin_list[j].strip() != "#":
                    split_hin = hin_list[j].split('\t')
                    if (split_hin[0] == "H"):
                        start_chunk = j
                        match = 0
                        for x in range(0, len(giza_list)):
                            # print(i,j)
                            split_giza = giza_list[x].split(' ')
                            # print(split_giza)
                            # print(split_eng)
                            # print(split_giza[0], split_eng[2].split('\n')[0], split_giza[1].split('\n')[0].strip(), split_hin[2])
                            # print(split_giza[1].split('\n')[0].strip() == split_hin[2])
                            if (split_giza[0].strip() == split_eng[2].split('\n')[0].strip() and split_giza[1].split('\n')[0].strip() == split_hin[2].strip()):
                                match = 1
                                # print("match: ", match)
                                break

                        if (match == 1):
                            break
                    j = j + 1
                flag = 0
                if (match == 0):
                    # print(i,j)
                    print(eng_list[i].strip())
                    i = i + 1
                    while eng_list[i].split('\t')[0] != "H" and eng_list[i].strip() != "#":
                        print(eng_list[i].strip())
                        i = i + 1
                    i = i - 1
                else:
                    print(hin_list[j].strip())
                    j = j + 1
                    while(hin_list[j].split('\t')[0] != "H" and hin_list[j].strip() != "#"):
                        print(hin_list[j].strip())
                        j = j + 1
            elif split_eng[0] == "H":
                print(eng_list[i].strip())
                i = i + 1
                while eng_list[i].split('\t')[0] != "H" and eng_list[i].strip() != "#":
                    print(eng_list[i].strip())
                    i = i + 1
                i = i - 1

            j = start
            if (eng_list[i].strip() == "#"):
                i = i - 1
            i = i + 1

        j = start
        while hin_list[j].strip() != "#":
            j = j + 1

    i = i + 1
    j = j + 1
