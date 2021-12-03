# read in lines
# take command and move horizontal or vertical
# move by number in line

f = open('input.txt', 'r')
lines = f.readlines()

x = 0
depth = 0
aim = 0

for line in lines:
  cmd, amt = line.split()
  amt = int(amt)
  if(cmd == 'forward'):
    x += amt
    depth += aim*amt
  elif(cmd == 'down'):
    aim += amt
  elif(cmd == 'up'):
    aim -= amt

print(x) # 2010
print(depth) # 1034321
print(aim) # 1030
print(x*depth) # 2078985210
