#include <vector>
#include <iostream>
using namespace std;

void solve(int n, int b, int h, int w, vector<int> price, vector<vector<int>> beds) {
	//write solution here. print output e.g. cout << "stay home" << endl;
}

int main() {
	int n,b,h,w;
	cin >> n >> b >> h >> w;
	vector<int> price;
	price.reserve(h);
	vector <vector<int>> beds;
	beds.resize(h, vector<int>(w));
	for (int i = 0; i < h; i++){
		cin >> price[i];
		for (int j = 0; j < w; j++){
			cin >> beds[i][j];
		}
	}

	solve(n,b,h,w,price,beds);
	return 0;
}
