# load binary lines
# count 1 0 of columns
# make new gamma string of mighest num in each column
# epsilon string is flipped binary of gamma
# power consumption is gamma * epsilon numbers

lines = open('input.txt', 'r').read().splitlines()

gamma = ""
epsilon = ""

for i in range(len(lines[0])):
  count = 0
  for ii in lines:
    if(ii[i] == '1'):
      count += 1
      
  if(count > len(lines)/2):
    gamma += "1"
    epsilon += "0"
  else:
    gamma += "0"
    epsilon += "1"

power = int(gamma,2) * int(epsilon,2)

print(gamma, int(gamma,2)) # 000010111110 190
print(epsilon, int(epsilon,2)) # 111101000001 3905
print(power) # 741950