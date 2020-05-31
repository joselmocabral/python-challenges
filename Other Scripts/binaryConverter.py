def binary_array_to_number(arr):
  index = 1
  sum = 0
  arr.reverse()
  for i in arr:
      sum += index * i
      index *= 2
  return sum
