from nltk import sent_tokenize
from nltk.corpus import reuters
from textrank.precompute import tokenize
import pickle
import math

class TfIdf:

	def __init__(self,document):
		self.document=document
		self.tf=[]
		self.idf=pickle.load(open("./textrank/idf.pkl","rb"))
		self.vector = []

	def term_frequency(self):
		self.sentences=sent_tokenize(self.document)
		#self.sentences=[set(tokenize(sentence)) for sentence in self.sentences]
		for sentence in self.sentences:
			words=tokenize(sentence)
			terms=set(words)
			freq=dict.fromkeys(terms,0)
			for word in words:
				freq[word]+=1
			self.tf.append(freq)

	def tfidf_vector(self):
		for i in range(len(self.sentences)):
			sentence=set(tokenize(self.sentences[i]))
			#print (sentence)
			tfidf={}
			for term in sentence:
				try:
					tfidf[term]=self.tf[i][term]*self.idf[term]
				except:
					tfidf[term]=self.tf[i][term]*math.log(len(reuters.fileids()))
			#print (tfidf)
			self.vector.append(tfidf)

