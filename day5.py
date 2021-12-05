from collections import defaultdict, namedtuple
from math import copysign

Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['p0', 'p1'])

def isHorizontal(line: Line):
  return line.p0.y == line.p1.y

def isVertical(line: Line):
  return line.p0.x == line.p1.x

def parseLine(lineStr: str) -> Line:
  [p0Str, _, p1Str] = lineStr.split(" ")
  return Line(parsePoint(p0Str), parsePoint(p1Str))

def parsePoint(pointStr: str) -> Point:
  coordStrings = pointStr.split(",")
  return Point(int(coordStrings[0]), int(coordStrings[1]))

def mySign(number):
  if abs(number) == 0:
    return 0
  else:
    return copysign(1, number)

def pointsCoveredBy(line: Line):
  points = []

  xStep = mySign(line.p1.x - line.p0.x)
  yStep = mySign(line.p1.y - line.p0.y)


  x = line.p0.x
  y = line.p0.y

  points.append(Point(x, y))

  while x != line.p1.x or y != line.p1.y:
    x += xStep
    y += yStep
    points.append(Point(x, y))

  return points


with open("day5-input.txt") as f:
  numCoverings = defaultdict(lambda: 0)
  numHorOrVertCoverings = defaultdict(lambda: 0)

  for line in f:
    line = parseLine(line)

    if isHorizontal(line) or isVertical(line):
      for point in pointsCoveredBy(line):
        numHorOrVertCoverings[point] += 1

    for point in pointsCoveredBy(line):
      numCoverings[point] += 1

  print("Part 1:")
  print(len([p for p in numHorOrVertCoverings if numHorOrVertCoverings[p] >= 2]))
  print("Part 2:")
  print(len([p for p in numCoverings if numCoverings[p] >= 2]))
