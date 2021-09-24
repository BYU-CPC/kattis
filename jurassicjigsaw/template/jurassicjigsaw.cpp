#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(vector<string> &samples, vector<vector<int>> &edges)
{
	//YOUR CODE HERE
	return -1;
}

int main(){
	int n, k;
	cin >> n >> k;

	vector<string> samples;
	vector<vector<int>> edges;
	string s;
	for (int i=0; i<n; i++)
       	{
		cin >> s;
		samples.push_back( s );
	}

	int min_unlikeliness = solve(samples, edges);
	cout << min_unlikeliness << endl;

	for (int e=0; e<edges.size(); e++)
	{
		cout << edges[e][0] << edges[e][1] << endl;
	}
	return 0;
}

