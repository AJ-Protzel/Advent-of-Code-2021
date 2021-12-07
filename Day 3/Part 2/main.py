import numpy as np

# get life support rating by oxygen gen rating * co2 scrub rating
# use first bit of a line
# keep only from bit criteria, discard others until 1 number
# checkf rom left to right
# oxygen gen rating = most common 0/1 in bit position, 1 for tie
# co2 scrub rateing = least common | |
# turn binary into int for number

lines = open('input.txt', 'r').read().splitlines()

for i in range(len(lines)):
  lines[i] = [int(item) for item in lines[i]]

lines = np.array(lines)

oxy = lines
co2 = lines

i = 0
while len(oxy) > 1:
  oxy = oxy[np.argsort(oxy[:,i])] # sort
  bit = np.count_nonzero(oxy == 1, axis = 0) # count

  if(bit[i] >= len(oxy)/2): # bit = 1
    oxy = np.delete(oxy, slice(0,len(oxy)-bit[i]), axis=0) # delete 0
  else: # bit = 0
    oxy = np.delete(oxy, slice(len(oxy)-bit[i], len(oxy)), axis=0) # delete 1
  i += 1

i = 0
while len(co2) > 1:
  co2 = co2[np.argsort(co2[:,i])] # sort
  bit = np.count_nonzero(co2 == 1, axis = 0) # count

  if(bit[i] >= len(co2)/2): # bit = 1
    co2 = np.delete(co2, slice(len(co2)-bit[i], len(co2)), axis=0) # delete 1
  else: # bit = 0
    co2 = np.delete(co2, slice(0,len(co2)-bit[i]), axis=0) # delete 0
  i += 1

oxy = int((''.join(str(i) for i in oxy[0])),2)
co2 = int((''.join(str(i) for i in co2[0])),2)
life = oxy * co2

print(oxy) # 256
print(co2) # 3205
print(life) # 903810