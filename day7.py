from math import inf

with open("day7-input.txt") as f:
  positions = [int(num) for num in f.read().strip().split(',')]

# ==== PART 1 ====
# https://en.wikipedia.org/wiki/Geometric_median
# No easy and exact way to calculate it seems
# Maybe I'll just try everything -- should probably work in 1D
minPos, maxPos = min(positions), max(positions)
minCost = inf
argMinCost = None

for finalPos in range(minPos, maxPos + 1): # Clearly cannot be outside the range of numbers
  cost = sum(abs(pos - finalPos) for pos in positions)
  if cost < minCost:
    argMinCost = finalPos
    minCost = cost


print(f"Part 1: {minCost}")

# ==== PART 2 ====
def fuelCost(distance):
  # https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
  return distance * (distance + 1) // 2

minCost = inf
argMinCost = None

for finalPos in range(minPos, maxPos + 1): # Clearly cannot be outside the range of numbers
  # https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
  cost = sum(fuelCost(abs(pos - finalPos)) for pos in positions)
  if cost < minCost:
    argMinCost = finalPos
    minCost = cost

print(f"Part 2: {minCost}")