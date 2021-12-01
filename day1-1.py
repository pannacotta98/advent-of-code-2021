with open("day1-1-input.txt") as _input:
  numbers = [int(number) for number in _input]
  numIncreases = 0
  for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
      numIncreases += 1
  print(numIncreases)