#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(vector<vector<int>> &rooms, int num_to_close_off)
{
	//YOUR CODE HERE
	return -1;
}

int main(){
	int N, k;
	cin >> N >> k;
	vector<vector<int>> rooms;
	int l, r;
	for (int i=0; i<N; i++)
       	{
		cin >> l >> r;
		vector<int> row;
		row.push_back(l);
		row.push_back(r);
		rooms.push_back( row );
	}

	cout << solve(rooms, k) << endl;
	return 0;
}
