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
#include <queue>
#include <iostream>
#include <functional>
#include <algorithm>
#include <fstream>
#include <limits>

using namespace std;

class Edge {
public:
	Edge(int i, double w) { id = i; weight = w; }
	int id;
	double weight;
	bool operator<(const Edge& rhs) const {
		if (this->weight > rhs.weight)
			return true;
		else
			return false;
	}
};

void DijkstraShortestReach::run()
{
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */
	double inf = numeric_limits<double>::infinity();
	ifstream in("Data/DijkstraShortestReach.txt");
	int T;
	in >> T;

	for (int t = 0; t<T; t++) {
		int N, M;
		in >> N >> M;
		vector<vector<Edge>> adj(N);
		vector<bool> marked(N); fill(marked.begin(), marked.end(), false);
		vector<int> edgeTo(N); fill(edgeTo.begin(), edgeTo.end(), -1);
		vector<double> distTo(N); fill(distTo.begin(), distTo.end(), inf);
		priority_queue<Edge, vector<Edge>> pq;

		for (int m = 0; m<M; m++) {
			int x, y, r;
			in >> x >> y >> r;
			adj[x - 1].push_back(Edge(y - 1,r)); // undirected
			adj[y - 1].push_back(Edge(x - 1,r));
		}

		int S;
		in >> S;

		pq.push(Edge(S - 1,0));
		distTo[S - 1] = 0;
		while (!pq.empty()) {
			Edge s = pq.top();
			marked[s.id] = true;
			pq.pop();
			for (unsigned int i = 0; i< adj[s.id].size(); i++) {
				Edge e = adj[s.id][i];
				if (!marked[e.id]) {
					pq.push(e);
					if (distTo[e.id]>distTo[s.id] + e.weight) {
						distTo[e.id] = distTo[s.id] + e.weight;
					}
				}
			}
		}

		bool first = true;
		for (int i = 0; i<N; i++) {
			if (i != S - 1) {
				if (!first)
					cout << " ";

				if (distTo[i] == inf) {
					cout << "-1";
					first = false;
				}
				else {
					cout << distTo[i];
					first = false;
				}
			}
		}
		cout << endl;
	}
}