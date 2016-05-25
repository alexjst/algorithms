/*
https://www.hackerrank.com/challenges/dijkstrashortreach

Given a graph consisting N nodes (labelled 1 to N) where a specific given node S represents the starting position S and an edge between two nodes is of a given length, which may or may not be equal to other lengths in the graph.

It is required to calculate the shortest distance from the start position (Node S) to all of the other nodes in the graph.

Note 1: If a node is unreachable , the distance is assumed as -1.

Input Format

The first line contains T, denoting the number of test cases.
First line of each test case has two integers N, denoting the number of nodes in the graph and M, denoting the number of edges in the graph.

The next M lines each consist of three space-separated integers x,y,r, where x and y denote the two nodes between which the undirected edge exists, r denotes the length of edge between these corresponding nodes.

The last line has an integer S, denoting the starting position.

Constraints
1<=T<=10
2<=N<=3000
1<=M<=N*(N-1)/2
1<=x,y,S<=N
1<=r<=350




If there are edges between the same pair of nodes with different weights, they are to be considered as is, like multiple edges.

Output Format

For each of the T test cases, print a single line consisting N-1 space separated integers denoting the shortest distance of N-1 nodes from starting position S.

For unreachable nodes, print -1.

*/
#include "DijkstraShortestReach.h"

#include <vector>
#include <iostream>

using namespace std;

void DijkstraShortestReach::run()
{
    int T;
    cin >> T;

    for (int t = 0; t<T; t++) {
        vector<vector<int>> adj;
        vector<bool> marked;
        vector<int> edgeTo;
        vector<int> distTo;

        int N, M;
        cin >> N >> M;
        adj.resize(N);
        marked.resize(N); fill(marked.begin(), marked.end(), false);
        edgeTo.resize(N); fill(edgeTo.begin(), edgeTo.end(), -1);
        distTo.resize(N); fill(distTo.begin(), distTo.end(), -1);
        for (int m = 0; m<M; m++) {
            int v, w;
            cin >> v >> w;
            adj[v - 1].push_back(w - 1);
            adj[w - 1].push_back(v - 1);
        }
        int S;
        cin >> S;
        queue<int> bfsQueue;
        bfsQueue.push(S - 1);
        marked[S - 1] = true;
        distTo[S - 1] = 0;
        while (!bfsQueue.empty()) {
            int s = bfsQueue.front();
            bfsQueue.pop();
            for_each(adj[s].begin(), adj[s].end(), [&](int i) {
                if (!marked[i]) {
                    bfsQueue.push(i);
                    marked[i] = true;
                    edgeTo[i] = s;
                    distTo[i] = distTo[s] + 6;
                }
            });
        }
        for (int i = 0; i<N; i++) {
            if (i != (S - 1))
                cout << distTo[i] << " ";
        }
        cout << endl;
    }
}