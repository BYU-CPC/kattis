#include <iostream>
#include <vector>
using namespace std;

int solve(int n, int p, vector<int> nums){
	//YOUR CODE HERE
	return 0;
}

int main(){
	int n, p;
	cin >> n >> p;
	vector<int> v;
	for(int i = 0; i < n; i++){
		int m = 0;
		cin >> m;
		v.push_back(m);
	}
	
	cout << solve(n, p, v) << endl;
	return 0;
}


