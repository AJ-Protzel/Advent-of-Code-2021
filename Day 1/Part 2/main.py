# read in numbers
# sum 3 numbers and compare to sum of next three
# if next sum is greater then count++

f = open('input.txt', 'r')
lines = f.readlines()

count = 0
for i in range(len(lines)-3):
  s1 = int(lines[i])+int(lines[i+1])+int(lines[i+2])
  s2 = int(lines[i+1])+int(lines[i+2])+int(lines[i+3])
  if(s2 > s1):
    count += 1

print(count) # 1518
