# Smallest multiple

# The smallest positive number that is evenly divisible by all of the numbers from 1 to n

def smallestMultiple(n):
	num = n
	while True:
		if (all(num%i == 0 for i in range(1, n+1))) == True:
			break
		else:
			num += n
	return num
