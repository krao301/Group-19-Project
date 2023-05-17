# Converts the Code-Mixed Chunks to Code-Mixed Sentences.

import sys
with open(sys.argv[1], 'r') as f:
    for line in f:
        if (line.split('_')[0] != "Sentence" and line.split('\t')[0] != "H"):
            print(line.split('\t')[2].strip(), end=" ")

        elif line.split('_')[0] == "Sentence":
            print('\n')
