class Graph:
  def __init__(self):
    self.graph = defaultdict(list)
  def addEdge(self, a, b):
    self.graph[a].append(b)
  def DFSUtil(self, b, visited):
    visited.add(b)
    print(b, end=' ')
     self.graph[b]:
        self.DFSUtil(neighbour, visited)
  def DFS(self, b):
    visited = set()
    self.DFSUtil(b, visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2)


