aim = 0
forward = 0
depth = 0

with open("day2-input.txt") as f:
  for line in f:
    [direction, valueString] = line.split(" ")
    value = int(valueString)
    if direction == "forward":
      forward += value
      depth += aim * value
    elif direction == "down":
      aim += value
    elif direction == "up":
      aim -= value

print(depth * forward)

    