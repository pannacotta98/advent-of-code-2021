testInput = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".splitlines()

# digitsWithUniqueNumberOfSegments = {1: 2, 4: 4, 7: 3, 8: 7}
uniqueNumberOfSegments = [2, 4, 3, 7]
# digitsWithNumberOfSegments[numSegments] is a list of the numbers
# shown with numSegments segments
digitsWithNumberOfSegments = [
  [],        # 0
  [],        # 1
  [1],       # 2
  [7],       # 3
  [4],       # 4
  [2, 3, 5], # 5
  [0, 6, 9], # 6
  [8],       # 7
]

digitsSegments = [
  "abcefg",  # 0
  "cf",      # 1
  "acdeg",   # 2
  "acdfg",   # 3
  "bcdf",    # 4
  "abdfg",   # 5
  "abdefg",  # 6
  "acf",     # 7
  "abcdefg", # 8
  "abcdfg",  # 9
]

def parseLine(line):
  [uniquePatterns, outputDigits] = [x.split() for x in line.split(" | ")]
  return uniquePatterns, outputDigits

def friendlyDictPrint(dictionary):
  print("{")
  for key, item in dictionary.items():
    print(f"  {key}: {item}")
  print("}")


def solvePart1(inputLines):
  part1Ans = 0
  for line in inputLines:
    _, outputDigits = parseLine(line)
    part1Ans += sum(1 for digit in outputDigits if len(digit) in uniqueNumberOfSegments)
  return part1Ans

def solvePart2(inputLines):
  part2Ans = 0
  for line in inputLines:
    uniquePatterns, outputDigits = parseLine(line)
    digitMapping = dict()
    reverseDigitMapping = dict()

    # Find the easy ones (unique number of segments)
    for patternStr in uniquePatterns:
      pattern = frozenset(patternStr)
      possibleDigits = digitsWithNumberOfSegments[len(pattern)]

      if len(possibleDigits) == 1:
        digitMapping[pattern] = possibleDigits[0]
        reverseDigitMapping[possibleDigits[0]] = pattern

    # Try to do the rest
    for patternStr in uniquePatterns:
      pattern = frozenset(patternStr)
      if len(pattern) in uniqueNumberOfSegments:
        continue

      if len(pattern) == 5: # possible digits: [2, 3, 5]
        if reverseDigitMapping[1] < pattern:
          digitMapping[pattern] = 3
          reverseDigitMapping[3] = pattern
        elif (reverseDigitMapping[4] - reverseDigitMapping[1]) < pattern:
          digitMapping[pattern] = 5
          reverseDigitMapping[5] = pattern
        else:
          digitMapping[pattern] = 2
          reverseDigitMapping[2] = pattern

      elif len(pattern) == 6: # possible digits: [0, 6, 9]
        if reverseDigitMapping[4] < pattern:
          digitMapping[pattern] = 9
          reverseDigitMapping[9] = pattern
        elif (reverseDigitMapping[4] - reverseDigitMapping[1]) < pattern:
          digitMapping[pattern] = 6
          reverseDigitMapping[6] = pattern
        else:
          digitMapping[pattern] = 0
          reverseDigitMapping[0] = pattern
    
    # friendlyDictPrint(digitMapping)
    output = 0
    oom = [1000, 100, 10, 1]
    for i in range(len(outputDigits)):
      output += oom[i] * digitMapping[frozenset(outputDigits[i])]

    part2Ans += output

  return part2Ans



with open("day8-input.txt") as f:
  puzzleInput = [line for line in f]

print(f"Part1: {solvePart1(puzzleInput)}")
print(f"Part2: {solvePart2(puzzleInput)}")

# print(f"TEST: {solvePart2([testInput[0]])}")
# print(f"TEST: {solvePart2(['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'])}")

# This got kinda messy; for sure the trickiest one yet
# Might revisit and make less horrible... or not?