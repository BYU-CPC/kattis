#include <iostream>
using namespace std;

string encode(string message) {
	return "";
}

string decode(string message) {
	return "";
}


int main() {
	string type, message;
	cin >> type >> message;
	if(type == "E")
		cout << encode(message) << endl;
	else
		cout << decode(message) << endl;
}
