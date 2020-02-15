# Largest prime factor

# What is the largest prime factor of the number

def largestPrimeFactor(num):
	prime, maxi = 2, 1
	while prime <= num:
		if num % prime == 0:
			maxi = prime
			num = num // prime
		else:
			prime += 1
	return maxi

