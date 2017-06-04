import math

class Similarity:

	def __init__(self,tfidf):
		self.tfidf=tfidf
		self.vectors=tfidf.vector
		self.length=len(self.vectors)
		self.magnitude=[]

	def compute_magnitudes(self):
		for vector in self.vectors:
			square_sum=0
			for v in vector.values():
				square_sum=square_sum+(v**2)
			self.magnitude.append(math.sqrt(square_sum))

	def build_similarity_matrix(self):
		self.compute_magnitudes()
		# print (self.magnitude)
		self.matrix=[[0]*self.length for i in range(self.length)]
		for i in range(self.length):
			for j in range(i+1):
				s1=set(self.vectors[i].keys())
				s2=set(self.vectors[j].keys())
				words=s1.intersection(s2)
				#print (words)
				dot=0
				for word in words:
					dot=dot+(self.vectors[i][word]*self.vectors[j][word])
				self.matrix[i][j]=dot/(self.magnitude[i]*self.magnitude[j])
				self.matrix[j][i]=self.matrix[i][j]

	
