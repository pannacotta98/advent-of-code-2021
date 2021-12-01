windowSize = 3

with open("day1-1-input.txt") as _input:
  numbers = [int(number) for number in _input]

numIncreases = 0
for i in range(0, len(numbers)-windowSize):
  prevWindow = sum(numbers[i : i+windowSize])
  currentWindow = sum(numbers[i+1 : i+1+windowSize])
  if currentWindow > prevWindow:
    numIncreases += 1

print(numIncreases)