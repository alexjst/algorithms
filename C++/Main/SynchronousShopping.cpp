/*
https://www.hackerrank.com/contests/w20/challenges/synchronous-shopping

Bitville is a seaside city that has  shopping centers connected via  bidirectional roads. Each road connects exactly two distinct shopping centers and has a travel time associated with it.

There are  different types of fish sold in Bitville. Historically, any shopping center has a fishmonger selling certain types of fish. Buying any amount of fish from any fishmonger takes no time.

Our heroes, Big Cat and Little Cat, are standing at Bitville shopping center number . They have a list of the types of fish sold at each fishmonger, and they want to collectively purchase all  types of fish in a minimal amount of time. To do this, they decide to split the shopping between themselves in the following way:

Both cats choose their own paths, starting at shopping center  and ending at shopping center . It should be noted that Little Cat's path is not necessarily the same as Big Cat's.
While traveling their respective paths, each cat will buy certain types of fish at certain shops.
When the cats reach shopping center , they must have collectively purchased all  types of fish in a minimal amount of time.
If one cat finishes shopping before the other, he waits at shopping center  for his partner to finish; this means that the total shopping time is the maximum of Little and Big Cats' respective shopping times.
It is to be noted that any of the cats can visit the shopping center  in between, but they both have to finish their paths at the shopping center .

Given the layout for Bitville and the list of fish types sold at each fishmonger, what is the minimum amount of time it will take for Big and Little Cat to purchase all  types of fish and meet up at shopping center ?

Input Format

The first line contains  space-separated integers:  (the number of shopping centers),  (the number of roads), and  (the number of types of fish sold in Bitville), respectively.

Each line  of the  subsequent lines () describes a shopping center as a line of space-separated integers. Each line takes the following form:

The first integer, , denotes the number of types of fish that are sold by the fishmonger at the  shopping center.
Each of the  subsequent integers on the line describes a type of fish sold by that fishmonger. Which is denoted by .
Each line  of the  subsequent lines () contains  space-separated integers describing a road. The first two integers,  and , describe the two cities it connects. The third integer, , denotes the amount of time it takes to travel the road (i.e., travel time).

Constraints

All  are different for every fixed .
Each road connectes  distinct shopping centers (i.e., no road connects a shopping center to itself).
Each pair of shopping centers is directly connected by no more than  road.
It is possible to get to any shopping center from any other shopping center.
Each type of fish is always sold by at least one fishmonger.
Output Format

Print the minimum amount of time it will take for the cats to collectively purchase all  fish and meet up at shopping center .

Sample Input

5 5 5
1 1
1 2
1 3
1 4
1 5
1 2 10
1 3 10
2 4 10
3 5 10
4 5 10
Sample Output

30
Explanation

Big Cat can choose the following route: , and buy fish at all of the shopping centers on his way.

Little Cat can choose the following route: , and buy fish from the fishmonger at the  shopping center only.
*/
#include "SynchronousShopping.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>

using namespace std;

struct Node {
	int id;
	vector<pair<int, int> > adj; // center id and distance/weight to it
	int dist; // dist to single source
	set<int> fish;

	Node(int _id) { id = _id; }
	Node() {}
	int getFishNum() { return fish.size();  }

	bool operator<(const Node& that) const {
		return this->dist > that.dist;
	}
};

Node joinFish(const Node& from, const Node& to, const int weight) {
	Node n = to;
	n.fish.insert(from.fish.begin(), from.fish.end());
	n.dist = from.dist + weight;
	return n;
}

void SynchronousShopping::run()
{
	ifstream in("data/SynchronousShopping.txt");

	int N, M, K;
	in >> N >> M >> K;

	vector<Node> graph(N);
	
	for (int n = 0; n < N; n++) {
		graph[n].id = n;
		// read n'th shopping center
		int T;
		in >> T; // number of fish types at n'th center
		for (int t = 0; t < T; t++) {
			int A;
			in >> A; // one type of fish
			graph[n].fish.insert(A);
		}
	}

	for (int m = 0; m < M; m++) {
		int x, y, z;
		in >> x >> y >> z;
		graph[x - 1].adj.push_back(make_pair(y - 1, z));
		graph[y - 1].adj.push_back(make_pair(x - 1, z));
	}
	in.close();

	// posible destinations
	vector<Node> destinations;

	// priority queue with shortest distance to source on top
	int result = -1;
	priority_queue<Node> pq;
	graph[0].dist = 0;
	pq.push(graph[0]);
	while (!pq.empty()) {
		Node cur = pq.top();
		if (cur.id == N - 1) {
			for (auto dest : destinations) {
				// check if dest and cur have combined fish set complete, if so, return results. 
				Node checker = joinFish(cur, dest, 0);
				if (checker.fish.size() == K) {
					result = max(cur.dist, dest.dist);
					break; // break out two loops
				}
			}

			if (result > 0) // break out the outer loop when result is found
				break;

			destinations.push_back(cur);
		}
		pq.pop();
		for (auto nbr : cur.adj) {
			Node n = joinFish(cur, graph[nbr.first], nbr.second);
			pq.push(n);
		}
	}
	cout << result;
}