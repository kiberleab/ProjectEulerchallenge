# 10001st prime

# The nth prime number

def isPrime(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True

def nthPrime(n):
	num  = 2
	nums = []
	while len(nums) < n:
		if isPrime(num) == True:
			nums.append(num)
		num += 1
	return nums[-1]
