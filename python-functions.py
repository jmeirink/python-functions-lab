# Challenge #1  - Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  print(sum)
  return sum

sum_to(8)

# Challenge #2 - Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num
  print(largest)
  return largest

largest([1, 2, 4, 8])


# Challenge #3 - Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

def occurrences(string, substr):
  stripped_string = string.replace(substr, '')
  return (len(string) - len(stripped_string)) // len(substr)

occurrences('fleep floop', 'e')

# Challenge #4 - Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  print(product)
  return product

product(2,7, 8)