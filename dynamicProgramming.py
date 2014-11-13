import random
import numpy

#Not a correct solution

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

def binHandler(M,P,S,R):
	choice = 0
	i = len(M) - 2
	while i >= 0:
		for j in range(i + 1, len(M)):
			if distance(M[i], M[j]) >= k:
				R[i] = M[j]
				choice = 1
				break
		if choice == 1:
			S[i] = max(P[i] + S[j], S[i+1])
		else:
			S[i] = S[i+1]
		i -= 1
	print S, R 

def maxprofits(M, P, S, k):
	maxProf = 0
	global tempProfit	
	tempProfit = 0
	R = numpy.arange(10)
	i = 0
	binHandler(M,P,S,R)

if __name__ == "__main__":
	
	arrayLen = 10
	#distances each city is from the start of QVH

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
	print "Sorted distances: ", dist	
	print "Profits: ", profs

	profit = maxprofits(dist, profs, S, k)
	
	print "Max Profit: ", S[0]
