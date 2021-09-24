#include <iostream>
#include <string>
#include <vector>
using namespace std;

string solve(string msg)
{
	//YOUR CODE HERE
	return "";
}

int main(){
	int N;
	cin >> N;

	string msg;
	getline(cin,msg); // grab newline char
	for (int i=0; i<N; i++)
       	{
		getline(cin, msg);
		cout << solve(msg) << endl;
	}

}

