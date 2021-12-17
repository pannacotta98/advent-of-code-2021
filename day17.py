# # Example: "target area: x=20..30, y=-10..-5"
# # Target range
# xMin, xMax = 20, 30
# yMin, yMax = -10, -5

# My input: "target area: x=117..164, y=-140..-89"
# Target range
xMin, xMax = 117, 164
yMin, yMax = -140, -89

# Just gonna do some brute force with arbitrary boundaries hehe
# I feel like there almost def is a better way, maybe even closed form
# solution
highestValidYPos = 0
validInitialVelocities = []
for vx0 in range(-300, 300):
  if vx0 % 50 == 0: print("vx0", vx0)
  for vy0 in range(-300, 300):
    # print("vy0", vy0)
    x, y = 0, 0
    vx, vy = vx0, vy0
    highest = 0

    for _ in range(0, 1000):
      x += vx
      y += vy
      if vx != 0:
        vx += -1 if vx > 0 else 1
      vy -= 1

      # print("    ", y)
      if y > highest:
        highest = y

      if xMin <= x <= xMax and yMin <= y <= yMax:
        if highest > highestValidYPos:
          highestValidYPos = highest
        validInitialVelocities.append((vx0, vy0))
        break

print("Part 1:", highestValidYPos)
# print(validInitialVelocities)
print("Part 2:", len(validInitialVelocities))

# Certainly not proud of this
