#include <iostream>
#include <vector>
#include <stack>
#include <unordered_set>

using namespace std;

class Graph {
public:
    int vertices;
    vector<vector<int>> adjacencyList;

    Graph(int V) : vertices(V), adjacencyList(V) {}

    void addEdge(int u, int v) {
        adjacencyList[u].push_back(v);
        adjacencyList[v].push_back(u);  // Assuming an undirected graph
    }

    void DFS(int startNode) {
        stack<int> s;
        unordered_set<int> visited;

        s.push(startNode);
        visited.insert(startNode);

        cout << "DFS Traversal:" << endl;

        while (!s.empty()) {
            int current = s.top();
            s.pop();
            cout << current << " ";

            for (int neighbor : adjacencyList[current]) {
                if (visited.find(neighbor) == visited.end()) {
                    s.push(neighbor);
                    visited.insert(neighbor);
                }
            }
        }

        cout << endl;
    }
};

int main() {
    Graph g(6);  // Example with 6 vertices

    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);
    g.addEdge(2, 5);

    int startNode = 0;
    g.DFS(startNode);

    return 0;
}
