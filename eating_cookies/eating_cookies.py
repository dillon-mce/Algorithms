#!/usr/bin/python

import sys

# Caching outside of the recursive call, because the answer for a given n will never change. Even more efficient.
cache = {0: 1}
def eating_cookies(n, unused_cache=None):
  if n < 0:
    return 0

  try:
    return cache[n]
  except:
    answer = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    cache[n] = answer
    return answer
  
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')