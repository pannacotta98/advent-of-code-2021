from collections import Counter
from functools import cache


def parseRules(rulesStr):
  rules = {}
  for line in rulesStr.splitlines():
    temp = line.strip().split(" -> ")
    rules[temp[0]] = temp[1]
  return rules

@cache
def recursiveSolve(polymer, depth, maxDepth):
  global rules

  if depth == maxDepth:
    return Counter()
  counter = Counter()
  for i in range(len(polymer) - 1):
    pair = polymer[i] + polymer[i + 1] # concat
    toInsert = rules[pair]
    counter.update(toInsert)
    subPolymer = polymer[i] + toInsert + polymer[i + 1]
    counter += recursiveSolve(subPolymer, depth + 1, maxDepth)
  return counter


with open("day14-input.txt") as f:
  [polymer, rulesStr] = f.read().strip().split("\n\n")
  rules = parseRules(rulesStr.strip())

# ==== Part 1 ====
counter = Counter(polymer)
steps = 10
depth = 0
counter += recursiveSolve(polymer, depth, maxDepth=steps)
[mostCommon, *_, leastCommon] = counter.most_common()
# print(counter)
print("Part 1: ", mostCommon[1] - leastCommon[1])

# ==== Part 2 ====
counter = Counter(polymer)
steps = 40
depth = 0
counter += recursiveSolve(polymer, depth, maxDepth=steps)
[mostCommon, *_, leastCommon] = counter.most_common()
# print(counter)
print("Part 2: ", mostCommon[1] - leastCommon[1])
