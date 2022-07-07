#include <bits/stdc++.h>
using namespace std;
class Graph {
public:
  map<int, bool> visited;
  map<int, list<int> > adj;
  void addEdge(int n, int o);
  void DFS(int n);
};

void Graph::addEdge(int n, int o)
{
  adj[n].push_back(o);
}

void Graph::DFS(int n)
{
  visited[n] = true;
  cout << n << " ";
  list<int>::iterator i;
  for (i = adj[n].begin(); i != adj[n].end(); ++i)
    if (!visited[*i])
      DFS(*i);
}
int main()
{
  Graph g;
  g.addEdge(0, 1);
  g.addEdge(0, 2);
  g.addEdge(1, 2);
  g.addEdge(2, 0);
  g.addEdge(2, 3);
  g.addEdge(3, 3);

  cout << "Following is Depth First Traversal"
      " (starting from vertex 2) \n";
  g.DFS(2);

  return 0;
}


