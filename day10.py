# puzzleInput = """[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]""".splitlines()

matchingPairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
illegalCloserPoints = {")": 3, "]": 57, "}": 1197, ">": 25137}
autoCompletePoints = {")": 1, "]": 2, "}": 3, ">": 4}

with open("day10-input.txt") as f:
  puzzleInput = [line for line in f]

part1Ans = 0
corruptedLines = []
for line in puzzleInput:
  stack = []
  for char in line:
    if char in matchingPairs:
      stack.append(char)
    elif char in matchingPairs.values():
      if char != matchingPairs[stack.pop()]:
        part1Ans += illegalCloserPoints[char]
        corruptedLines.append(line)
        break

for corruptedLine in corruptedLines:
  puzzleInput.remove(corruptedLine)
scores = []
for line in puzzleInput:
  stack = []
  score = 0
  for char in line:
    if char in matchingPairs:
      stack.append(char)
    elif char in matchingPairs.values():
      if char != matchingPairs[stack.pop()]:
        print("This should never happen")
  while stack:
    score *= 5
    score += autoCompletePoints[matchingPairs[stack.pop()]]
  scores.append(score)
scores.sort()
part2Ans = scores[len(scores) // 2]  

print("Part 1:", part1Ans)
print("Part 2:", part2Ans)

# Quick and dirty today