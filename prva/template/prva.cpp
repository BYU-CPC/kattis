#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solve(int r, int c, vector<vector<char>> grid){
	//YOUR CODE HERE
	return "";
}

int main() {
	int r, c;
	cin >> r >> c;
	vector<vector<char>> v;
	v.resize(r, vector<char>(c));

	for(int i = 0; i < r; i++) {
		for(int j = 0; j < c; j++) {
			cin >> v[i][j];
		}
	}

	cout << solve(r, c, v) << endl;
	return 0;
}
