import numpy as np
import matplotlib.pyplot as plt

def parsePointLine(line):
  [x, y] = line.strip().split(",")
  return (int(x), int(y))

def parseFoldLine(line):
  [dimension, coord] = line.split(" ")[2].split("=")
  return [dimension, int(coord)]

def paperFromPoints(points):
  maxCoord = np.max(points, axis=0)
  paper = np.zeros(maxCoord + [1, 1], dtype=np.bool8)
  for point in points:
    paper[tuple(point)] = True
  return paper

def printPaper(paper):
  print(paper.T * 1)

def showPaper(paper):
  plt.imshow(paper.T)
  plt.colorbar()
  plt.show()

def foldPaper(paper, dimension, coord):
  if dimension == "y":
    aboveFold = paper[:, :coord]
    belowFold = paper[:, coord+1:]
    aboveFoldHeight = aboveFold.shape[1]
    belowFoldHeight = belowFold.shape[1]
    padSize = aboveFoldHeight - belowFoldHeight
    paddedAndFlippedBelowFold = np.pad(np.flip(belowFold, axis=1), [(0, 0), (padSize, 0)])
    result = aboveFold + paddedAndFlippedBelowFold
    return result
  elif dimension == "x":
    aboveFold = paper[:coord, :]
    belowFold = paper[coord+1:, :]
    leftOfFoldWidth = aboveFold.shape[0]
    rightOfFoldWidth = belowFold.shape[0]
    padSize = leftOfFoldWidth - rightOfFoldWidth
    paddedAndFlippedBelowFold = np.pad(np.flip(belowFold, axis=0), [(padSize,0), (0, 0)])
    result = aboveFold + paddedAndFlippedBelowFold
    return result

def solvePart1(points, folds):
  paper = paperFromPoints(markedPoints)
  return np.count_nonzero(foldPaper(paper, folds[0][0], folds[0][1]))

def solvePart2(points, folds):
  paper = paperFromPoints(markedPoints)
  for fold in folds:
    paper = foldPaper(paper, fold[0], fold[1])
  return paper
  

with open("day13-input.txt") as f:
  [markingsInput, foldInput] = f.read().split("\n\n")

markedPoints = np.array([parsePointLine(line) for line in markingsInput.splitlines()])
folds = [parseFoldLine(line) for line in foldInput.splitlines()]

print("Part 1: ", solvePart1(markedPoints, folds))
print("Part 2: ")
part2 = solvePart2(markedPoints, folds)
np.set_printoptions(linewidth=100)
showPaper(part2)
