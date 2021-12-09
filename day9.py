import numpy as np
from scipy.ndimage import label
# Begin using some libraries today, numpy seems like a good thing to know
# Still need some practice doe hehe...

data = np.genfromtxt("day9-input.txt", delimiter=1, dtype=np.int32)

riskLevelSum = 0
for x in range(len(data)):
  for y in range(len(data[x])):
    adjCandidates = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    adjIndices = [ij for ij in adjCandidates
      if -1 < ij[0] < len(data)
      and -1 < ij[1] < len(data[x])]
    minAdj = min([data[ij] for ij in adjIndices])
    if data[x,y] < minAdj:
      riskLevelSum += 1 + data[x,y]

print(f"Part 1: {riskLevelSum}")

# ==== Part 2 ====
basinMask = data != 9
labeledArray, numFeatures = label(basinMask)

basinSizes = [np.count_nonzero(labeledArray == i) for i in range(1, numFeatures + 1)]
basinSizes.sort(reverse=True)

print(f"Part 1: {basinSizes[0] * basinSizes[1] * basinSizes[2]}")
