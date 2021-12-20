import numpy as np
from scipy.signal import correlate2d
import matplotlib.pyplot as plt

kernel = np.array([[256, 128, 64], [32, 16, 8], [4, 2, 1]])

def showImage(img):
  plt.imshow(img)
  plt.colorbar()
  plt.show()

def iterativEnhance(image, algorithm, iterations):
  img = np.array(image == "#", dtype=np.bool8)
  for i in range(iterations):
    img = imageEnhance(img, algorithm, i)
  return np.count_nonzero(img)

def imageEnhance(binImage, algorithm, iteration):
  fillVal = algorithm[0] == "#"
  if iteration % 2 == 0:
    fillVal = not fillVal
  lookupIndices = correlate2d(binImage, kernel, mode="full",
                              boundary="fill", fillvalue=fillVal)
  result = np.zeros_like(lookupIndices, dtype=np.bool8)
  for pos, pixel in np.ndenumerate(lookupIndices):
    result[pos] = algorithm[pixel] == "#"
  return result


with open("day20-input.txt") as f:
  algorithm, imageStr = f.read().strip().split("\n\n")

image = np.array([list(line.strip()) for line in imageStr.splitlines()])
print("Part 1:", iterativEnhance(image, algorithm, 2))
print("Part 2:", iterativEnhance(image, algorithm, 50))
