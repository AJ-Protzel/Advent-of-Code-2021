# read in numbers
# count++ if new number is greater than last

f = open('input.txt', 'r')
lines = f.readlines()

count = 0
old = lines.pop()
for line in lines:
  if(int(line) > int(old)):
    count += 1
  old = line
print(count) # 1482
