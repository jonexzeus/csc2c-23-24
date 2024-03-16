#include <iostream>
#include <vector>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

int tsp(const vector<vector<int>>& graph, int pos, int visited, vector<vector<int>>& dp, vector<vector<int>>& path) {
    if (visited == ((1 << graph.size()) - 1)) {
        return graph[pos][0]; // Return to starting city
    }
    
    if (dp[pos][visited] != -1) {
        return dp[pos][visited];
    }

    int ans = INF;
    int nextCity = -1;
    
    for (int i = 0; i < graph.size(); ++i) {
        if ((visited & (1 << i)) == 0 && graph[pos][i] > 0) { 
            int newAns = graph[pos][i] + tsp(graph, i, visited | (1 << i), dp, path);
            if (newAns < ans) {
                ans = newAns;
                nextCity = i;
            }
        }
    }

    path[pos][visited] = nextCity; // Store the next city in the path

    return dp[pos][visited] = ans;
}

void printPath(const vector<vector<int>>& path, int start, int visited) {
    int currentCity = start;
    cout << "Approximate shortest route: " << static_cast<char>('A' + currentCity) << " ";

    while (visited != ((1 << path.size()) - 1)) {
        int nextCity = path[currentCity][visited];
        cout << "-> " << static_cast<char>('A' + nextCity) << " ";
        currentCity = nextCity;
        visited |= (1 << nextCity);
    }

    cout << endl;
}

int main() {
    vector<vector<int>> graph = {
        {0, 50, 25, 30},
        {50, 0, 30, 10},
        {30, 10, 0, 15},
        {25, 10, 15, 0}
    };
    
    int n = graph.size();
    vector<vector<int>> dp(n, vector<int>(1 << n, -1));
    vector<vector<int>> path(n, vector<int>(1 << n, -1));

    int shortestRouteLength = tsp(graph, 0, 1, dp, path);
    
    cout << "Approximate shortest route length: " << shortestRouteLength << endl;

    // Print the path taken
    printPath(path, 0, 1);

    return 0;
}
