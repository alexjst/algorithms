/*

https://www.hackerrank.com/challenges/bfsshortreach

Given an undirected graph consisting of  nodes (labelled 1 to N) where a specific given node  represents the start position and an edge between any two nodes is of length  units in the graph.

It is required to calculate the shortest distance from start position (Node S) to all of the other nodes in the graph.

Note 1: If a node is unreachable , the distance is assumed as .
Note 2: The length of each edge in the graph is  units.

Input Format

The first line contains , denoting the number of test cases.
First line of each test case has two integers , denoting the number of nodes in the graph and , denoting the number of edges in the graph.
The next  lines each consist of two space separated integers , where  and  denote the two nodes between which the edge exists.
The last line of a testcase has an integer , denoting the starting position.

Constraints




Output Format

For each of  test cases, print a single line consisting of  space-separated integers, denoting the shortest distances of the N-1 nodes from starting position . This will be done for all nodes same as in the order of input 1 to N.

For unreachable nodes, print .

Sample Input

2
4 2
1 2
1 3
1
3 1
2 3
2
Sample Output

6 6 -1
-1 6
Explanation

For test cases 1:

The graph given in the test case is shown as :

Graph

S denotes the node 1 in the test case and B,C and D denote 2,3 and 4. Since S is the starting node and the shortest distances from it are (1 edge, 1 edge, Infinity) to the nodes B,C and D (2,3 and 4) respectively.

Node D is unreachable, hence -1 is printed (not Infinity).

For test cases 2: There are only one edge (2, 3) in a graph with 3 nodes, so node 1 is unreachable from node 2, and node 3 has one edge from node 2, each edge has the length of 6 units. So we output -1 6.
*/

#include "BfsShortestReach.h"

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Graph {
public:
    Graph(int N) { V.resize(N); for (int i = 0; i<N; i++) V[i] = i; }
    void AddEdge(int p, int q) {}
private:
    vector<int> V;
    vector<int> Adj;
};

void runTest() {
    int N, M;
    cin >> N >> M;
    for (int m = 0; m<M; m++) {

    }
}

void BfsShortestReach::run()
{
    /*
    Sample Input

        2
        4 2
        1 2
        1 3
        1
        3 1
        2 3
        2
    */

    int T;
    cin >> T;
    for (int t = 0; t<T; t++) {
        runTest();
    }
}
