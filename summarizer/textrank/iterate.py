
class Iterate:
	
	def __init__(self,similarity):
		self.d=0.85
		self.similarity=similarity
		self.length=similarity.length
		self.matrix=similarity.matrix
		self.computation()
	
	def computation(self):
		self.sum_weights=[0 for i in range(self.length)]
		for i in range(self.length):
			for j in range(self.length):
				self.sum_weights[i]+=self.matrix[i][j]

	def convergence(self,prev,curr):
		for i in range(self.length):
			if abs(curr[i]-prev[i])>0.001:
				return False
		return True

	def solve(self):
		prev=[2 for i in range(self.length)]
		curr=[10 for i in range(self.length)]
		while not self.convergence(prev,curr):
			prev=[i for i in curr]
			for i in range(self.length):
				temp=0
				for j in range(self.length):
					temp=temp+((self.matrix[j][i]/self.sum_weights[j])*(prev[j]))
				curr[i]=(1-self.d)+self.d*(temp)
		return curr