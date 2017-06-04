from nltk.tokenize import word_tokenize
from nltk.corpus import reuters
import pickle
import string
import math

def tokenize(data):
	punctuations=list(string.punctuation)
	words=word_tokenize(data)
	words=[w.lower() for w in words]
	words=[w for w in words if w not in punctuations]
	return words

def compute_idf():
	words=set()
	for fileid in reuters.fileids():
		tokens=tokenize(reuters.raw(fileid))
		words.update(tokens)
	idf=dict.fromkeys(words,0)
	for fileid in reuters.fileids():
		tokens=set(tokenize(reuters.raw(fileid)))
		for token in tokens:
			idf[token]+=1
	total=len(reuters.fileids())
	for word in words:
		idf[word]=math.log(total/(1+idf[word]))
	return idf

def write_to_file(idf):
	file=open("idf.pkl","wb")
	pickle.dump(idf,file)
	file.close()

write_to_file(compute_idf())