# Multiples of 3 and 5

# Find the sum of all the multiples of 3 or 5

def multiplesOf3and5(num):
	nums = []
	for n in range(num):
		if n%5 == 0 or n%3 == 0:
			nums.append(n)
	return sum(nums)
