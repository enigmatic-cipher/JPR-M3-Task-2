"""
Given an array of integer as input, find out which of the first or last element is larger and change all the values of the array to that. Print the changed array.
Input-> [4,8,12,20,6]
Output-> 6,6,6,6,6
"""

ls = [4,8,12,20,6]
ln = len(ls)
d = 0
f = 0
max = 0
for i in range(0,ln):
  d = ls[0]
  f = ls[ln-1]
  if (d>f):
    max = d
  else:
    max = f
for i in range(0,ln):
  ls[i] = max
print(ls)
