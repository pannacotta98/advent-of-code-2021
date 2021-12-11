import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

convKernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

def showMatrix(matrix):
  plt.imshow(matrix)
  plt.colorbar()
  plt.show()

def doIteration(inp):
  out = inp + 1

  allFlashing = np.zeros_like(out)
  while out[out > 9].any():
    currentlyFlashing = out > 9
    flashSpreading = convolve2d(currentlyFlashing, convKernel, mode="same", boundary="fill", fillvalue=0)
    out += flashSpreading
    out[currentlyFlashing > 0] = 0
    allFlashing += currentlyFlashing

  out[allFlashing > 0] = 0
  flashesInStep = np.count_nonzero(allFlashing)
  didAllFlash = np.all(allFlashing)

  return out, flashesInStep, didAllFlash

# Part 1
data = np.genfromtxt("day11-input.txt", delimiter=1, dtype=np.int32)
part1Ans = 0
for iteration in range(100):
  data, flashes, didAllFlash = doIteration(data)
  part1Ans += flashes

# Part 2
data = np.genfromtxt("day11-input.txt", delimiter=1, dtype=np.int32)
part2Ans = None
iteration = 0
while True:
  iteration += 1
  data, flashes, didAllFlash = doIteration(data)
  if didAllFlash:
    part2Ans = iteration
    break

print("Part 1:", part1Ans)
print("Part 2:", part2Ans)
