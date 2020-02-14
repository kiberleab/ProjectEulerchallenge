# Even Fibonacci numbers

# Find the sum of the even-valued terms.

def fiboEvenSum(num):
  f = [1,2]
  while f[-1] < num:
    f.append(f[-1] + f[-2])
  fSum = sum(n for n in f[:-1] if n%2==0)
  return fSum
