with open("day3-input.txt") as f:
  lines = [line for line in f]

numBits = len(lines[0].strip())
numZeros = [0] * numBits
numOnes = [0] * numBits

for line in lines:
  for i in range(0, numBits):
    if line[i] == "1":
      numOnes[i] += 1
    elif line[i] == "0":
      numZeros[i] += 1

gammaStr = ''.join("1" if ones >= zeros else "0" for zeros,ones in zip(numZeros, numOnes))
epsilonStr = ''.join("1" if zeros >= ones else "0" for zeros,ones in zip(numZeros, numOnes))

print(int(gammaStr, base=2) * int(epsilonStr, base=2))
