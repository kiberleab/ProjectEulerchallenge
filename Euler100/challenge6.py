# Sum square difference

# The squares of the first n natural numbers and the square of the sum.

def sumSquareDifference(n):
	sumSq = sum(range(1, n+1))**2
	sqSum = sum(i**2 for i in range(1, n+1))
	return sumSq - sqSum
