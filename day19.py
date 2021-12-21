from io import StringIO
import numpy as np
from numpy.linalg import matrix_power
from itertools import combinations

# Borrowing this part for now =================================================
# https://github.com/zedrdave/advent_of_code/blob/master/2021/19/__main__.py
rot90_x = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
rot90_y = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
rot90_z = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
# 24 rotations:
rots = [rot1@rot2
        for rot1 in [matrix_power(rot90_x, i) for i in range(4)]
        for rot2 in [matrix_power(rot90_y, i) for i in range(4)] + [matrix_power(rot90_z, i) for i in [1, 3]]]
# =============================================================================

def dist(p0, p1):
  return np.linalg.norm(p1 - p0)

def manhattanDist(p0, p1):
  return np.linalg.norm(p1 - p0, ord=1)

def generateDistances(beaconPositions):
  # Hopefully the number of occurences of distances are low enough
  # that a set is enough
  return {dist(p0, p1) for p0, p1 in combinations(beaconPositions, 2)}

class Scanner:
  def __init__(self, dataStr):
    firstLine, theRest = dataStr.split("\n", 1)
    self.id = int(firstLine.split(" ")[2])
    s = StringIO(theRest)
    self.beaconPos = np.genfromtxt(s, dtype=np.int32, delimiter=",")
    self.distances = generateDistances(self.beaconPos)
    self.pos = np.array([0, 0, 0]) if self.id == 0 else None

  def commonDistances(self, other):
    return self.distances.intersection(other.distances)

  def allDistTo(self, point):
    return {dist(point, p) for p in self.beaconPos}

  def tryMatching(self, other):
    matches = [(p1, p2) for p1 in self.beaconPos for p2 in other.beaconPos
               if len(self.allDistTo(p1) & other.allDistTo(p2)) >= 12]

    if not matches:
      return False

    # Find the rotation that makes the matching points match
    scannerRotation = next(filter(lambda rot: len({tuple(b1 - (b2 @ rot)) for b1, b2 in matches}) == 1, rots))
    # Which can then be used to find the offset/scanner position,
    # I'd imagine any point could be used at this point
    scannerPos = matches[0][0] - matches[0][1] @ scannerRotation
    # This transformation can also be applied to the other points in other
    absolutePos = [(pos @ scannerRotation) + scannerPos for pos in other.beaconPos]
    other.beaconPos = absolutePos
    other.pos = scannerPos
    
    return absolutePos


with open("day19-input.txt") as f:
  scannerInputs = f.read().strip().split("\n\n")

scanners = [Scanner(d) for d in scannerInputs]

positionedScanners = [scanners[0]]
remainingScanners = scanners[1:]
# Scanner 0 sets absolute pos and rot
absolutePositions = {tuple(pos) for pos in positionedScanners[0].beaconPos}

while remainingScanners:
  scannerToMatch = remainingScanners.pop(0)
  # Try to match agains some positioned scanner
  for sc in positionedScanners:
    absPos = sc.tryMatching(scannerToMatch)
    if absPos:
      absolutePositions.update([tuple(pos) for pos in absPos])
      positionedScanners.append(scannerToMatch)
      break
  else:
    # Failed; put it back and try again later
    remainingScanners.append(scannerToMatch)
      

print("Part 1:", len(absolutePositions))
maxScannerDistance = max(manhattanDist(sc0.pos, sc1.pos)
                         for sc0, sc1 in combinations(positionedScanners, 2))
print("Part 2:", int(maxScannerDistance))

# Worst day, no doubt
# Cheated a bit hehe. This was nice:
# https://github.com/zedrdave/advent_of_code/blob/master/2021/19/__main__.py