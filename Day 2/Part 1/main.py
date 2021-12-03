# read in lines
# take command and move horizontal or vertical
# move by number in line

f = open('input.txt', 'r')
lines = f.readlines()

x = 0
y = 0

for line in lines:
  cmd, amt = line.split()
  amt = int(amt)
  if(cmd == 'forward'):
    x += amt
  elif(cmd == 'down'):
    y += amt
  elif(cmd == 'up'):
    y -= amt

print(x) # 2010
print(y) # 1030
print(x*y) # 2070300
