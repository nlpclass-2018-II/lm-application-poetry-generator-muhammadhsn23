import nltk
import random
from collections import Counter


file = open('_poetry_khairil_anwar.txt')
poem = file.read()	

token = nltk.word_tokenize(poem)

# NLTK shortcuts :)
bigrams = nltk.bigrams(token)
cfd = nltk.ConditionalFreqDist(bigrams)

# pick a random word
word = random.choice(token)

for i in range(15):
    print word,
    if word in cfd:
        word = random.choice(list(cfd[word].keys()))
    else:
        break