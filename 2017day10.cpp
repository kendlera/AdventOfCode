#include <vector>
#include <iostream> 
#include <algorithm>
#include <string>

using namespace std;

int input_part_one[] = {187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216};
// int input[] = {3, 4, 1, 5};

vector<int> this_is_gunna_be_dumb(vector<int> values, int current, int end) {
	vector<int> new_vector (values);
	int goal = end;
	while (current != goal) {
		new_vector[current] = values[end];
		end--;
		current++;
		if (end == -1) { end = 255; }
		if (current == 256) { current = 0; }
		// cout << end << endl;
	}
	new_vector[current] = values[end];
	return new_vector;
}

void densify_that_shit(vector<int> values) {
	// densify the hash
	int start;
	for (int i = 0; i < 16; i++) {
		start = i*16;
		int x = values[start];
		cout << start << ":";
		for (int j = 1; j < 16; j++) {
			cout << start+j << ":";
			x = (x ^ values[start+j]);
		}
		cout << endl;
		cout << hex << x << ":";
		cout << dec << endl;
	}
	cout << endl;
}

vector<int> calculate_input(string input) {
	vector<int> ans;
	for (auto item : input) {
		ans.push_back(int(item));
	}
	int arr[] = {17, 31, 73, 47, 23};
	vector<int> suffix (arr, arr+sizeof(arr)/sizeof(arr[0]));
	ans.insert(ans.end(), suffix.begin(), suffix.end());
	return ans;
}

int part_one() {
	vector<int> values;
	for (int i = 0; i < 256; i++) {
		values.push_back(i);
	}
	vector<int> input = calculate_input("187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216");
	// vector<int> input = calculate_input("");
	int current = 0;
	int skip = 0;
	int end_point;
	for (int rounds = 0; rounds < 64; rounds++) {
		for (int i = 0; i < input.size(); i++) {
			end_point = (current + input[i]) % 256;
			// cout << "current: " << current << "; end: " << end_point << endl;
			if (end_point < current) {
				// do something less elegant if we wrapped around
				end_point --;
				if (end_point < 0) { end_point = 255; }
				values = this_is_gunna_be_dumb(values, current, end_point);
			} else {
				reverse(values.begin()+current, values.begin()+end_point);
			}
			current = (end_point + skip) % 256;
			skip++;
		}
		for (auto a : values) { cout << a << ":"; }
		cout << endl; 
	}
	cout << skip << endl;
	for (auto a : values) { cout << a << ":"; }
	cout << endl; 
	densify_that_shit(values);
	// cout << values.at(0) * values.at(1) << " is our result" << endl;
	return 0;
}

int main() {
	part_one();
	// 58dad07fa1d2d32c100df879a8069c0f not the right hash :(
	return 0;
}