def multiplesOf3and5(num):
  nums = []
  for n in range(num):
    if n%5 == 0 or n%3 == 0:
      nums.append(n)
  return sum(nums)
