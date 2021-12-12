class Graph:
  def __init__(self, vertices):
    self.adjList = {v: [] for v in vertices}
    
  def addEdge(self, v0, v1):
    # Assume undirected graph
    self.adjList[v0].append(v1)
    self.adjList[v1].append(v0)

  def part1(self):
    def traverse(vertex, visited):
      if vertex == "end":
        return 1

      if not vertex.isupper() and vertex in visited:
        return 0

      newVisited = visited.copy()
      newVisited.add(vertex)
      numPaths = 0

      for adjacent in self.adjList[vertex]:
        numPaths += traverse(adjacent, newVisited)

      return numPaths

    visited = set()
    numPaths = traverse(vertex="start", visited=visited)
    return numPaths

  def part2(self):
    # Yayy, code duplication
    def traverse(vertex, visited):
      if vertex == "end":
        return 1

      if vertex == "start" and visited["start"] > 0:
        return 0

      if (not vertex.isupper()
          and visited[vertex] > 0
          and (any(visits > 1 for v, visits in visited.items() if not v.isupper()))):
        return 0

      newVisited = visited.copy()
      newVisited[vertex] += 1
      numPaths = 0

      for adjacent in self.adjList[vertex]:
        numPaths += traverse(adjacent, newVisited)

      return numPaths

    visited = {v: 0 for v in self.adjList}
    numPaths = traverse(vertex="start", visited=visited)
    return numPaths

# puzzleInput = """start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end""".splitlines()

with open("day12-input.txt") as f:
  puzzleInput = [line.strip() for line in f]

allCaves = {cave for caves in puzzleInput for cave in caves.split("-")}

graph = Graph(allCaves)

for line in puzzleInput:
  [cave0, cave1] = line.split("-")
  graph.addEdge(cave0, cave1)

print("Part 1: ", graph.part1())
print("Part 2: ", graph.part2())
# Not super elegant today

