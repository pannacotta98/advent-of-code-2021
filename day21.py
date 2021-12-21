from itertools import cycle, product
from functools import cache

def boardPos(pos, move):
  return (pos + move - 1) % 10 + 1

def movePlayer(pos, score, die, dieRollNum):
  move = next(die) + next(die) + next(die)
  pos = boardPos(pos, move)
  score += pos
  return pos, score, dieRollNum + 3

def part1(p1Pos, p2Pos):
  p1Score = 0
  p2Score = 0

  die=cycle(range(1, 100 + 1))
  dieRollNum = 0
  while True:
    p1Pos, p1Score, dieRollNum = movePlayer(p1Pos, p1Score, die, dieRollNum)
    if p1Score >= 1000:
      return p2Score * dieRollNum

    p2Pos, p2Score, dieRollNum = movePlayer(p2Pos, p2Score, die, dieRollNum)
    if p2Score >= 1000:
      return p1Score * dieRollNum
  
def part2(p1Pos, p2Pos):
  p1Score = 0
  p2Score = 0

  @cache
  def traverseTree(p1Pos, p2Pos, p1Score, p2Score, isP1sTurn):
    if p1Score >= 21:
      return 1, 0

    if p2Score >= 21:
      return 0, 1

    p1Wins = 0
    p2Wins = 0

    if isP1sTurn:
      for perm in product([1, 2, 3], repeat=3):
        move = sum(perm)
        newPos = boardPos(p1Pos, move)
        newScore = p1Score + newPos
        p1ChildWins, p2ChildWins = traverseTree(newPos, p2Pos, newScore, 
                                                p2Score, not isP1sTurn)
        p1Wins += p1ChildWins
        p2Wins += p2ChildWins

    else:
      for perm in product([1, 2, 3], repeat=3):
        move = sum(perm)
        newPos = boardPos(p2Pos, move)
        newScore = p2Score + newPos
        p1ChildWins, p2ChildWins = traverseTree(p1Pos, newPos, p1Score, 
                                                newScore, not isP1sTurn)
        p1Wins += p1ChildWins
        p2Wins += p2ChildWins

    return p1Wins, p2Wins
      
  p1Wins, p2Wins = traverseTree(p1Pos, p2Pos, p1Score, p2Score, True)
  return max(p1Wins, p2Wins)


with open("day21-input.txt") as f:
  line0, line1 = f.read().strip().splitlines()
  p1Pos = int(line0.split(" ")[4])
  p2Pos = int(line1.split(" ")[4])

print("Part 1:", part1(p1Pos, p2Pos))
print("Part 2:", part2(p1Pos, p2Pos))
  