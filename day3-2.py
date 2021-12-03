with open("day3-input.txt") as f:
  lines = [line for line in f]

def oxygenFilterCondition(numZeros, numOnes):
  return "1" if numOnes >= numZeros else "0"

def CO2FilterCondition(numZeros, numOnes):
  return "0" if numOnes >= numZeros else "1"

def iterativeFiltering(lines, condition):
  numBits = len(lines[0].strip())

  for i in range(0, numBits):
    numZeros = 0
    numOnes = 0

    for line in lines:
      if line[i] == "1":
        numOnes += 1
      elif line[i] == "0":
        numZeros += 1

    valueToKeep = condition(numZeros, numOnes)

    lines = [line for line in lines if line[i] == valueToKeep]


    if len(lines) == 1:
      return lines[0]

oxygenStr = iterativeFiltering(lines, oxygenFilterCondition)
CO2Str = iterativeFiltering(lines, CO2FilterCondition)

print(int(oxygenStr, base=2) * int(CO2Str, base=2))
