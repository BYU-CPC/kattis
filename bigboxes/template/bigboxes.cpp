#include <vector>
#include <iostream>
using namespace std;

int solve(int n, int k, vector<int> weights){
	//write solution here
	return 0;
}

int main() {
	int n,k;
	cin >> n >> k;
	vector <int> weights;
	weights.reserve(n);
	for(int i = 0; i < n; i++){
		cin >> weights[i];
	}

	cout << solve(n, k, weights) << endl;
	return 0;
}
