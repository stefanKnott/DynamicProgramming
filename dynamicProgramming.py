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

def binHandle(M, P, S, R):

	i = len(dist) - 2
	while i >= 0:
		for j in range(i + 1, len(dist)):
			if distance(dist[i], dist[j]) >= k:
				choice = dist[j]
				R[i] = choice
				break
		S[i] = max(profs[i] + S[j], S[i+1])

		i -= 1
	print S
	
def maxprofits(M, P, S, k):
	maxProf = 0
	global tempProfit	
	tempProfit = 0
	n = 1		
	R = numpy.arange(10)
	binHandle(M, P, S, R)

if __name__ == "__main__":
	
	#distances each city is from the start of QVH
	global dist
	dist = numpy.arange(10)
	global profs
	profs = numpy.arange(10)
	S = numpy.arange(10)
	for i in range(10):
		#fills distances
		dist[i] = (int)(random.random() * float(i * 15))
		profs[i] = (int)(random.random() * float(i * 15))
		if i == 9:
			S[i] = profs[i]
		else:
			S[i] = 0
	
	mergeSort(0, 9)
	k = 10
	print dist	
	print profs

	profit = maxprofits(dist, profs, S, k)
	
	print S[0]
