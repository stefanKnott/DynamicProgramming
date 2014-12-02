import random
import numpy

def mergeSort(low, high):
	if low < high:
		middle = low + (high - low)/2
		mergeSort(low,middle)
		mergeSort(middle + 1, high)
		merge(low, middle, high)

def merge(low, middle, high):
	helper = numpy.arange(high + 1)
	for i in range(low, high + 1):
		helper[i] = dist[i]
	i, j, k = low, middle + 1, low

	while i <= middle and j <= high:
		if helper[i] <= helper[j]:
			dist[k] = helper[i]
			i += 1
		else:
			dist[k] = helper[j]
			j += 1
		k += 1

	while i <= middle:
		dist[k] = helper[i]
		k += 1
		i += 1

def distance(a, b):
	return b - a

def binHandler(M, P, S, k):
	if M is None or P is None or S is None or k is None:
		return -1
	if k < 0:
		return -1
	choice = 0
	i = len(M) - 2
	while i >= 0:
		for j in range(i+1, len(M)):
			if distance(M[i], M[j]) >= k:
			#	R[i] = M[j]
				choice = 1
				break
		if choice == 1:
			S[i] = max(P[i] + S[j], S[i+1])
		else:
			S[i] = S[i+1]
		i -= 1

#Solution to the following question: 
	"""
	Yuckdonalds is considering opening a series of restaurants along Quaint Valley Highway (QVH). The possible locations are along a straight line, and the distances of these locations from the start of QVH are, in miles and in increasing order, m1; m2; : : : ; mn
	The constraints are as follows: At each location, Yuckdonalds may open at most one restaurant. The expected profit from opening a restaurant at location i is pi, where pi > 0 and i = 1;2; : : : ; n
	Any two restaurants should be at least k miles apart, where k is a positive integer.
	"""

def maxProfWithDistConst():
	arrayLen = 10
	#distances each city is from the start of QVH
	global dist
	dist = numpy.arange(arrayLen)
	global S
	profs = numpy.arange(arrayLen)
	S = numpy.arange(arrayLen)
	for i in range(1, arrayLen):
		#fills distances
		dist[i] = (int)(random.random() * float(i * 15))
		profs[i] = (int)(random.random() * float(i * 15))
		if i == arrayLen - 1:
			S[i] = profs[i]
		else:
			S[i] = 0
	
	mergeSort(0, arrayLen - 1)
	k = 10
	profit = binHandler(dist, profs, S, k)
	print "Max profit with distance constraint problem:"
	print "Sorted distances: ", dist	
	print "Profits: ", profs
	print "Distance constraint: " + str(k)
	print "Max Profit: " + str(S[0]) + "\n"


def commonSubSeq(x, y, c):
	if x is None or y is None or c is None:
		return -1

	for i, x_letter in enumerate(x):
		for j, y_letter in enumerate(y):
			if i == 0 or j == 0:
				c[i,j] = 0
	
			if i > 0 and j > 0 and x_letter == y_letter:
				c[i,j] =  c[i-1, j-1] + 1
	
			if i > 0 and j > 0 and x_letter != y_letter:
				c[i,j] = max(c[i, j-1], c[i-1, j])

	#last index in matrix will hold the LCS value
	return c[len(x)-1][len(y)-1]

#Finds the longest common subsequence between 2 arrays terminated with a 0
def LCS():
	dnaSeq1 = 'ACACCCTGTAAATAGAAAC0'
	dnaSeq2 = 'ATAAGCTGTATATAGCACC0'

	common = numpy.zeros((len(dnaSeq1), len(dnaSeq2)))

	lcs = commonSubSeq(dnaSeq1, dnaSeq2, common)
	print "Longest common subsequence problem:"
	print "Sequence 1: " + str(dnaSeq1)
	print "Sequence 2: " + str(dnaSeq2)
	print "LCS: " + str(int(lcs)) + "\n"


def diff(a, b):
	if a == b:
		return 0
	else:
		return 1

def editDistance(x, y, e):
	for i, x_letter in enumerate(x):
		for j, y_letter in enumerate(y):
			if i == 0 or j == 0:
				if not diff(x_letter, y_letter):
					e[i,j] = 0
				else:
					e[i,j] = 1
			else:
				e[i,j] = min(1 + e[i-1,j], 1 + e[i, j-1], diff(x_letter, y_letter) + e[i-1, j-1])
	return e[len(x)-1, len(y)-1]

def editDist():
	word1 =  'snowy'
	word2 = 'sunny'

	edit = numpy.zeros((len(word1), len(word2)))

	editDist = editDistance(word1, word2, edit)

	print "Edit distance problem:"
	print "Word 1: " + word1
	print "Word 2: " + word2
	print "Edit Distance: " + str(editDist) + "\n"

if __name__ == "__main__":

	maxProfWithDistConst()
	LCS()
	editDist()
	
	

