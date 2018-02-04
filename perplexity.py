import sys
import nltk
import random
import collections
from collections import Counter

reload(sys)
sys.setdefaultencoding('utf8')

file = open('_poetry_khairil_anwar.txt')
poem1 = file.read()	

file = open('_poetry_test.txt')
test_text = file.read()

def unigram(a):
	#beri 0.01 utk kata yg tidak ada di dictionary
	jum_kata= 0
	model =a
	for f in model:
		model[f] = 0.01
	# model = collections.defaultdict(lambda: 0.01)
	for f in a:
		#klo udah ada di model tambah 1
		if(f in model):
			model[f] +=1
		else:
		#klo blm ada set 0.01
			model[f] =0.01
		jum_kata +=1
	for word in model:
		model[word] =model[word]/jum_kata
		# print (model[word])s
	return model

def perplexity(test, model):
	#rumus akar pangkat minus jumlah kata di data test , dalem akarnya probability tiap unigram data test
	test = nltk.word_tokenize(test)
	perplexity = 1
	n=0
	for word in test:
		perplexity = perplexity*(1/model[word])
		# print perplexity
		n+=1
	perplexity = pow(perplexity, 1/float(n))
	return perplexity


tokens = nltk.word_tokenize(poem1)
# model = unigram(poem1)
asd['a'] = 1
print(asd)
# print (perplexity(test_text, model))
# print(model)
