import nltk
import re
import pprint
from nltk import word_tokenize
import codecs
for i in codecs.open('../CL-1-Project/Hindi_Raw/1-15000.txt'):
    i = i.strip()
    print(" ".join(word_tokenize(i)))
