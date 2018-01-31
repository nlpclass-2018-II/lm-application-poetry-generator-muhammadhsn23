import nltk
import random
import sys
from collections import Counter

reload(sys)
sys.setdefaultencoding('utf8')


file = open('_poetry_khairil_anwar.txt')
poem = file.read()	

token = nltk.word_tokenize(poem)

# NLTK shortcuts :)
bigrams = nltk.ngrams(token,1)
cfd = Counter(nltk.ConditionalFreqDist(bigrams))



# for c in cfd:
# 	print Counter(cfd[c])

print "INI PALING ", cfd.most_common(10)

# print Counter(cfd)


# pick a random word
# word = random.choice(token)

# for i in range(15):
#     print word,
#     if word in cfd:
#         word = random.choice(list(cfd[word].keys()))
#     else:
#         break