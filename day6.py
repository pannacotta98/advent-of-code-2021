def fishIterations(initValues, iterations):
  # occurences[val] is the number of fish with the timer value val
  occurences = [0] * (8 + 1)
  for val in initValues:
    occurences[val] += 1

  for day in range(0,iterations):
    numNewFish = occurences[0] # also num fish to have timer reset
    occurences[:-1] = occurences[1:]
    occurences[6] += numNewFish
    occurences[-1] = numNewFish

  return occurences

with open("day6-input.txt") as f:
  timerValues = [int(num) for num in f.read().strip().split(",")]

print(f"Part 1: {sum(fishIterations(initValues=timerValues, iterations=80))}")
print(f"Part 2: {sum(fishIterations(initValues=timerValues, iterations=256))}")
