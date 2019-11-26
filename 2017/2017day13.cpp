#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

void part_one() {
	ifstream myfile ("input.txt");
	string separator = ": ";
	int pos;
	int severity = 0;
	string line;
	int token, range;
    if (myfile.is_open()) {
        while (getline (myfile,line)) {
        	pos = line.find(separator);
			token = stoi(line.substr(0, pos));
			line.erase(0, pos+2);
			range = stoi(line);
			// cout << token << " layer has range of " << range << endl;
			if (token > 1) {
				if ((token % ((range-1)*2)) == 0) {
					cout << "collided in " << token << " which has a range of " << range << endl;
					severity = severity + (token * range);
				}
			}
        }
        myfile.close();
    }
    cout << severity << " severity" << endl;
}

void build_system(int range, int offset, map<int, vector<int> >& range_offsets) {
	vector<int> offsets;
	int off_copy;
	map<int, vector<int> >::iterator it;
	if (range_offsets.find(range) == range_offsets.end()) {
		cout << "did not find " << range << endl;
		offsets.push_back(offset);
		range_offsets[range] = offsets;
	} else {
		cout << "found " << range << endl;
		if (find(offsets.begin(), offsets.end(), offset) == offsets.end()) { 	// we didn't find it
			cout << "adding " << offset << " to " << range << endl;
			range_offsets[range].push_back(offset);
		}
	}
}

int part_two() {
	/*
	 * the answer will be the first number not a multiple of the loop plus offset for all inputs 
	 */
	ifstream myfile ("input.txt");
	string separator = ": ";
	int pos;
	string line;
	int token, range, offset;
	map<int, vector<int> > range_offsets;
	cout << "opening file" << endl;
    if (myfile.is_open()) {
        while (getline (myfile,line)) {
        	pos = line.find(separator);
			token = stoi(line.substr(0, pos));
			line.erase(0, pos+2);
			range = (stoi(line)-1) * 2;
			// cout << token << " layer has range of " << range << endl;
			if (token <= 1) { 
				offset = token;
			} else {
				offset = token % range;
			}
			cout << "processing layer " << token << " with range of " << range << " and offset " << offset << endl;
			build_system(range, offset, range_offsets);
		}
		myfile.close();
	}
	// return 0;
	cout << range_offsets.size() << " ranges compiled" << endl;
	map<int, vector<int> >::iterator it1;
	vector<int> offsets;
	// vector<int>::iterator it2;
	bool found = false;
	bool caught;
	int delay = 0;
	while (!found) {
		caught = false;
		for (it1 = range_offsets.begin(); it1 != range_offsets.end(); it1++) {
			cout << "testing all offsets for range " << it1->first << endl;
			offsets = it1->second;
			for (int offset : offsets) {
				cout << "\toffset " << offset << endl;
				if (((delay+offset) % it1->first) == 0) { 
					caught = true;
					break;
				}
			}
			if (caught) { 
				cout << "caught in " << delay << endl;
				delay ++;
				break; 
			}
		}
		if (!caught) {
			return delay;
		}
	}
	return 0;


}

int main() {
	part_one();
	int delay = part_two();
	cout << "we must delay " << delay << " picoseconds" << endl;
	return 0;
}