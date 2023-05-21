#!/usr/bin/python3

"""determining the fewest number of coins needed 
to meet a given amount total"""

def makeChange(coins, total):
  coinValues = [float('inf')] * (total + 1)
  coinValues[0] = 0
  
  for eachCoin in coins:
    for i in range(eachCoin, total + 1):
      coinValues[i] = min(coinValues[i], coinValues[i - eachCoin] + 1)
      
  if coinValues[total] == float('inf'):
    return -1
  return coinValues[total]