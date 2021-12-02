depth = 0
forward = 0

with open("day2-input.txt") as f:
  for line in f:
    [direction, valueString] = line.split(" ")
    value = int(valueString)
    if direction == "forward":
      forward += value
    elif direction == "down":
      depth += value
    elif direction == "up":
      depth -= value

print(depth * forward)

    