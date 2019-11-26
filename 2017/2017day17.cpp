#include <iostream>
#include <string>
#include <vector>

using namespace std;

void part_one() {
	vector<int> buffer;
	buffer.push_back(0);
	int steps = 303;
	int current = 0;
	int pos;
	int part_two_answer;
	for (int value = 1; value < 50000001; value++) {
		pos = (steps + current) % value;
		if (pos == 0) { 
			cout << value << " comes after 0 now" << endl;
			part_two_answer = value; 
		}
		// commented out the buffer insert for part two
		// buffer.insert(buffer.begin()+pos+1, value);
		/* for (int nums: buffer) { cout << nums << "-"; }
		cout << endl; */
		current = pos+1;
	}
	for (int nums: buffer) { cout << nums << "-"; }
	cout << endl;
}

int main() {
	part_one();
	return 0;
}