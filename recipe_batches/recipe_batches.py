#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  lcd = None
  for key in recipe.keys():
    ingredients.setdefault(key, 0)
    number_for_ingredient = ingredients[key] // recipe[key]
    if lcd is None or number_for_ingredient < lcd:
      lcd = number_for_ingredient
  return lcd


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))