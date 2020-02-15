# Multiples of 3 and 5

# Find the sum of all the multiples of 3 or 5

def multiplesOf3and5(num):
	sums = sum(n for n in range(num) if n%3 == 0 or n%5 == 0)
	return sums
