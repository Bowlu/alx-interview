#!/usr/bin/python3

"""determining the fewest number of coins needed 
to meet a given amount total"""

def makeChange(coins, total):
    add = 0
    if total <= 0:
        return 0
 
    coins.sort(reverse=True)
 
    for coin in coins:
        if (total < coin):
            pass
        i, j = divmod(total, coin)
        total = j
        add += i
   
    if total != 0:
      return -1
    return add