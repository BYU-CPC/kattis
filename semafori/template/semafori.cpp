#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(vector<int>* locations, vector<int>* red_times, vector<int>* green_times, int road_length)
{
	//YOUR CODE HERE
	return -1;
}

int main(){
	int N, L;
	cin >> N >> L;
	vector<int>* locs    = new vector<int>();
	vector<int>* t_red   = new vector<int>();
	vector<int>* t_green = new vector<int>();
	int D,R,G;
	for (int i=0; i<N; i++)
       	{
		cin >> D >> R >> G;
		locs->push_back(D);
		t_red->push_back(R);
		t_green->push_back(G);
	}

	cout << solve(locs, t_red, t_green, L) << endl;
	return 0;
}
