import networkx as nx
import numpy as np

def createGraph(puzzleInput):
  G = nx.DiGraph()
  for (x, y), element in np.ndenumerate(puzzleInput):
    adjCandidates = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    adjIndices = [ij for ij in adjCandidates
      if -1 < ij[0] < len(puzzleInput)
      and -1 < ij[1] < len(puzzleInput[x])]

    for ij in adjIndices:
      G.add_edge((x,y), ij, weight=puzzleInput[ij])
  return G

# ==== Part 1 ====
puzzleInput = np.genfromtxt("day15-input.txt", delimiter=1, dtype=np.int32)
G1 = createGraph(puzzleInput)
part1Ans = nx.shortest_path_length(G1, source=(0,0), target=tuple(i - 1 for i in puzzleInput.shape), weight="weight")
print("Part 1:", part1Ans)

# ==== Part 2 ====
scale = 5
extendedPuzzleInput = np.zeros(shape=np.array(puzzleInput.shape) * scale, dtype=np.int32)
for i in range(scale):
  for j in range(scale):
    increase = i + j
    extendedPuzzleInput[
      i*puzzleInput.shape[0] : (i+1)*puzzleInput.shape[0],
      j*puzzleInput.shape[1] : (j+1)*puzzleInput.shape[1]
    ] = (puzzleInput + increase - 1) % 9 + 1

G2 = createGraph(extendedPuzzleInput)
part2Ans = nx.shortest_path_length(G2, source=(0,0), target=tuple(i - 1 for i in extendedPuzzleInput.shape), weight="weight")
print("Part 2:", part2Ans)
