#!/usr/bin/python3

"""Prime Game"""

def isWinner(x, nums):
  if x < 1 or not nums:
    return None
  
  maria = 0
  ben = 0
  
  n = max(nums)
  primeNum = [True] * (n + 1)
  primeNum[0] = primeNum[1] = False
  
  for i in range(2, int(n**0.5) + 1):
    if primeNum[i]:
      for j in range(i**2, n + 1, i):
        primeNum[j] = False
        
        
  for num in nums:
    count = sum(primeNum[2:n+1])
    ben += count % 2 == 0
    maria += count % 2 == 1
    
  if maria == ben:
    return None
  
  return 'Maria' if maria > ben else 'Ben'
  