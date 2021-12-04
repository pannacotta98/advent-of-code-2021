class BingoBoard:
  def __init__(self, boardAsString):
    self.numbers = [
      [number for number in row.split()] 
        for row in boardAsString.split("\n")]
    self.marked = [[False] * len(self.numbers) for _ in range(0, len(self.numbers[0]))]

  def mark(self, number):
    for i in range(0, len(self.numbers)):
      for j in range(0, len(self.numbers[i])):
        if self.numbers[i][j] == number:
          self.marked[i][j] = True

  def hasWon(self):
    for line in self.marked:
      if all(line):
        return True
    
    for column in zip(*self.marked):
      if all(column):
        return True

    return False

  def sumOfUnmarked(self):
    sumOfUnmarked = 0
    for i in range(0, len(self.numbers)):
      for j in range(0, len(self.numbers[i])):
        if not self.marked[i][j]:
          sumOfUnmarked += int(self.numbers[i][j])
    return sumOfUnmarked


def solvePart1(inputStr):
  [numberSequenceStr, *boardsStr] = inputStr.split("\n\n")
  numberSequence = numberSequenceStr.split(",")
  boards = [BingoBoard(boardStr) for boardStr in boardsStr]

  for number in numberSequence:
    for board in boards:
      board.mark(number)
      if board.hasWon():
        return board.sumOfUnmarked() * int(number)

def solvePart2(inputStr):
  [numberSequenceStr, *boardsStr] = inputStr.split("\n\n")
  numberSequence = numberSequenceStr.split(",")
  boards = [BingoBoard(boardStr) for boardStr in boardsStr]

  for number in numberSequence:
    i = 0
    while i < len(boards):
      boards[i].mark(number)
      if boards[i].hasWon():
        if len(boards) > 1:
          boards.remove(boards[i])
          i -= 1
        else:
          return boards[i].sumOfUnmarked() * int(number)
      i += 1

with open("day4-input.txt") as f:
  inputStr = f.read()

print(f"Part 1: {solvePart1(inputStr)}")
print(f"Part 2: {solvePart2(inputStr)}")
