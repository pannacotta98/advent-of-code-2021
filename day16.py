from math import prod

operators = {
  0: sum,
  1: prod,
  2: min,
  3: max,
  5: lambda x: 1 if x[0] > x[1] else 0,
  6: lambda x: 1 if x[0] < x[1] else 0,
  7: lambda x: 1 if x[0] == x[1] else 0
}

def hexToBinStr(hexStr):
  # number, pad, rjust, size, kind = 0xABC123EFFF, '0', '>', 42, 'b'
  # return f'{number:{pad}{rjust}{size}{kind}}'
  return f"{int(hexStr, 16):0{len(hexStr)*4}b}"

def parse(binStr):
  packetVersion = int(binStr[0:3], base=2)
  packetId = int(binStr[3:6], base=2)

  if packetId == 4:
    binNum = ""
    pos = 6
    moreBits = True
    while moreBits:
      moreBits = binStr[pos] == '1'
      binNum += binStr[pos+1 : pos+4+1]
      pos += 5
    val = int(binNum, base=2)
    return binStr[pos:], packetVersion, val

  else:
    typeId = binStr[6]
    accPacketVersion = packetVersion
    if typeId == '0':
      totalSubPacketLength = int(binStr[7 : 7 + 15], base=2)
      subPackages = binStr[7 + 15 : 7 + 15 + totalSubPacketLength]
      values = []
      while subPackages:
        subPackages, ver, val = parse(subPackages)
        accPacketVersion += ver
        values.append(val)
      val = operators[packetId](values)
      return binStr[7 + 15 + totalSubPacketLength :], accPacketVersion, val
    else: # '1'
      numSubPackages = int(binStr[7 : 7 + 11], base=2)
      remaining = binStr[7 + 11 :]
      values = []
      for _ in range(numSubPackages):
        remaining, ver, val = parse(remaining)
        accPacketVersion += ver
        values.append(val)
      val = operators[packetId](values)
      return remaining, accPacketVersion, val


with open("day16-input.txt") as f:
  binStr = hexToBinStr(f.read().strip())
_, versionSum, val = parse(binStr)
print("Part 1:", versionSum)
print("Part 2:", val)

# This was certainly something i'm not used to doing
