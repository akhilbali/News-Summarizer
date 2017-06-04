import math
from textrank.tfidf import TfIdf
from textrank.similarity import Similarity
from textrank.iterate import Iterate

class Summary:

	def __init__(self,text):
		self.text=text
		self.computations()
		self.scores=self.iterate.solve()
		self.rank=self.generate_ranks()

	def computations(self):
		self.tfidf=TfIdf(self.text)
		self.tfidf.term_frequency()
		self.tfidf.tfidf_vector()
		self.similarity=Similarity(self.tfidf)
		self.similarity.build_similarity_matrix()
		self.iterate=Iterate(self.similarity)

	def generate_ranks(self):
		sorted_scores=sorted(self.scores)
		sorted_scores.reverse()
		rank=[0 for i in range(len(self.scores))]
		for i in range(len(self.scores)):
			rank[i]=sorted_scores.index(self.scores[i])
		return rank

	def lines(self,num):
		num=min(num,len(self.tfidf.sentences))
		s=[self.tfidf.sentences[0]]
		if self.rank[0]>=num:
			num=num-1
		for i in range(1,len(self.scores)):
			if (self.rank[i]<num):
				s.append(self.tfidf.sentences[i])
		return s
