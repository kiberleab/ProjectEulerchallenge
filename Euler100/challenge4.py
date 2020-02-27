# Largest palindrome product

# Find the largest palindrome made from the product of two 3-digit numbers

def largestPalindromeProduct(n):
	nums = []
	upper = 10**n
	lower = 10**(n-1)
	for i in range(lower, upper):
		for j in range(lower, upper):
			if i*j == int(str(i*j)[::-1]):
				nums.append(i*j)
	return max(nums)
