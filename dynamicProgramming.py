import random

def mergesort(X):
	result = []
	if len(X) < 2:
		return X
	mid = int(len(X)/2)
	y = mergesort(X[:mid])
	z = mergesort(X[mid:])
	if y is None or z is None:
		return
	i = 0
	j = 0

	while i < len(y) and j < len(z):
		if y[i] > z[j]:
			result.append(z[j])
			j += 1
		else:
			result.append(y[i])
			i += 1
	result += y[i:]
	result += z[j:]
	return result


def distance(a, b):
	return b - a

def binHandle(parent, M, P, tmp, lc):

	lastchosen = lc
	i = parent
	left = 2*i
	right = 2*i + 1
	if left > len(M):
		return
	
	parent = M[parent]

	if right <= len(M) and left < len(M):	
		childRestL = M[left]
		childRestR = M[right]

		#choose best child
		if distance(lastchosen, childRestL) >= k:
			if P[right] > P[left]:
				outcome = P[right]
				lastchosen = M[right] 
				tmp += outcome
				
			else: 
				outcome = P[left]
				lastchosen = M[left]
				tmp += outcome
		else:
			if distance(lastchosen, childRestR) >= k:
				outcome = P[right]
				lastchosen = M[right]

		print outcome
		binHandle(lastchosen, M, P, tmp, lastchosen)
		
def maxprofits(M, P, k):
	maxProf = 0
	global tempProfit	
	tempProfit = 0
	n = 1		

	#test each index in array
	for n in range(1, len(M)):
		binHandle(n, M, P, tempProfit, 0)
		#if tempProfit > maxProf:
	#		maxProf = tempProfit
	#	tempProfit = 0
	return maxProf

if __name__ == "__main__":
	
	#distances each city is from the start of QVH
	dist = []
	profs = []
	for i in range(10):
		#fills distances
		dist.append((int)(random.random() * float(i * 15)))
		profs.append((int)(random.random() * float(i * 15)))

	dist = mergesort(dist)
	k = 10
	print dist	
	print profs

	profit = maxprofits(dist, profs, k)
	
	print profit
