# I'm gonna try doing it by manipulating the chars directly
# to avoid traveling up in the tree to find neighbors

from math import floor, ceil
import json
from itertools import permutations

def reduceSnailfishIteration(num):
  """Runs one iteration of reduce. Returns true if something changed"""

  # Check for exploding pairs
  nestedLevel = 0
  pos = 0
  while pos < len(num):
    if num[pos] == "[":
      nestedLevel += 1
      # pos += 1
      if nestedLevel == 5: # Explode
        leftVal = int(num[pos + 1])
        rightVal = int(num[pos + 3])
        # Add to left
        tempPos = pos - 1
        while tempPos > 0:
          if num[tempPos].isdigit():
            num[tempPos] = str(int(num[tempPos]) + leftVal)
            break
          tempPos -= 1
        # Add to right
        tempPos = pos + 4
        while tempPos < len(num):
          if num[tempPos].isdigit():
            num[tempPos] = str(int(num[tempPos]) + rightVal)
            break
          tempPos += 1
        # Replace pair with 0
        num[pos : pos + 5] = "0"
        return True
    elif num[pos] == "]":
      nestedLevel -= 1
    pos += 1

  # Check for splits
  pos = 0
  while pos < len(num) - 1:
    if num[pos].isdigit() and int(num[pos]) >= 10: # Split TODO FIX
      val = int(num[pos])
      left = floor(val/2)
      right = ceil(val/2)
      del num[pos]
      num.insert(pos, "]")
      num.insert(pos, str(right))
      num.insert(pos, ",")
      num.insert(pos, str(left))
      num.insert(pos, "[")
      return True
    pos += 1

  return False

def reduceSnailfish(num):
  shouldStop = False
  while not shouldStop:
    shouldStop = not reduceSnailfishIteration(num)

def snailfishMagnitude(numCharArray):
  num = "".join(numCharArray)
  nestedArray = json.loads(num)

  def magnitude(numArray):
    if isinstance(numArray, int):
      return int(numArray)
    left, right = numArray
    return 3*magnitude(left) + 2*magnitude(right)

  return magnitude(nestedArray)

def addSnailfish(num0, num1):
  result = ["[", *num0, ",", *num1, "]"]
  reduceSnailfish(result)
  return result
    
def printCharList(l):
  print("".join(l))


with open("day18-input.txt") as f:
  puzzleInput = [list(line.strip()) for line in f]

# ==== Part 1 ====
snailfishSum = puzzleInput[0]
printCharList(snailfishSum)
for num in puzzleInput[1:]:
  snailfishSum = addSnailfish(snailfishSum, num)
printCharList(snailfishSum)
print("Part 1:", snailfishMagnitude(snailfishSum))

# ==== Part 2 ====
largestMagnitude = 0
for num0, num1 in permutations(puzzleInput, 2):
  mag = snailfishMagnitude(addSnailfish(num0, num1))
  largestMagnitude = max(largestMagnitude, mag)

print("Part 2:", largestMagnitude)