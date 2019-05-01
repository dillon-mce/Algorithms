#!/usr/bin/python

import sys
from collections import namedtuple
from functools import reduce

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  values = sorted(items, key = weighted, reverse = True)
  bag = []

  for item in values:
    if item.size <= capacity:
      bag.append(item)
      capacity -= item.size
  
  total_value = reduce(sum_value, bag)
  total_cost = reduce(sum_size, bag)
  item_names = sorted([x.index for x in bag])

  print(f'Items to select: {item_names}\nTotal cost: {total_cost}\nTotal value: {total_value}')

  return {'Value': total_value, 'Chosen': item_names}


def weighted(item):
    return item.value / item.size
  
def sum_value(a, b):
  if type(a) is type(0):
    return a + b.value
  else:
    return a.value + b.value

def sum_size(a, b):
  if type(a) is type(0):
    return a + b.size
  else:
    return a.size + b.size

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')