#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(vector<int>* profits, vector<int>* costs, int min_to_retire)
{
	//YOUR CODE HERE
	return -1;
}

int main(){
	int n, M;
	cin >> n >> M;
	vector<int>* profits = new vector<int>();
	vector<int>* costs   = new vector<int>();
	int p_i, c_i;
	for (int i=0; i<n; i++)
       	{
		cin >> p_i >> c_i;
		profits->push_back( p_i );
		costs->push_back( c_i );
	}

	cout << solve(profits, costs, M) << endl;
	return 0;
}
