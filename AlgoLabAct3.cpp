#include <bits/stdc++.h>
using namespace std;

int n;
int graph[10][10];
bool visited[10];

void TSPUtil(int curr_pos, int cost) {
    if (cost >= 70)
        return;

    if (curr_pos == n - 1) {
        cost += graph[curr_pos][0];

        if (cost <= 70) {
            cout << "Approximate shortest route length: " << cost << endl;
            return;
        }

        return;
    }

    for (int i = 1; i < n; i++) {
        if (!visited[i] && graph[curr_pos][i] != 0) {
            visited[i] = true;
            TSPUtil(i, cost + graph[curr_pos][i]);
            visited[i] = false;
        }
    }
}

void TSP(int graph[][10]) {
    n = 4;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != j && graph[i][j] == 0)
                graph[i][j] = 1000000;
        }
    }

    visited[0] = true;
    TSPUtil(0, 0);
}

int main() {
    graph[0][1] = 50;
    graph[0][2] = 30;
    graph[0][3] = 25;
    graph[1][0] = 50;
    graph[1][2] = 40;
    graph[1][3] = 10;
    graph[2][0] = 30;
    graph[2][1] = 40;
    graph[2][3] = 15;
    graph[3][0] = 25;
    graph[3][1] = 10;
    graph[3][2] = 15;

    TSP(graph);

    return 0;
}