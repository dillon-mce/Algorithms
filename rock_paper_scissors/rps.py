#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n <= 0:
    return [[]]

  possible_values = [["rock"], ["paper"], ["scissors"]]
  if n == 1:
    return possible_values

  result = []
  rps_list = rock_paper_scissors(n - 1)
  for possible_value in possible_values:
    for value in rps_list:
      result.append(possible_value + value)
  return result
  
  
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')