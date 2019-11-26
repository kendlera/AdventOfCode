#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <queue>

using namespace std;
map<int, vector<int> > pipes;

int find_min_elem() {
	for (int i = 0; i < 2000; i++) {
		if (pipes.find(i) != pipes.end()) { return i; }
	}
	return -1;
}

int part_one() {
	ifstream myfile ("input.txt");
	string separator = " <-> ";
	string comma = ",";
	int pos, current, start;
	string line, token, elem;
    if (myfile.is_open()) {
        while (getline (myfile,line)) {
        	vector <int> connections;
			pos = line.find(separator);
			token = line.substr(0, pos);
			line.erase(0, pos+5);
			while ((pos = line.find(comma)) != string::npos) {
				elem = line.substr(0, pos);
				connections.push_back(stoi(elem));\
				line.erase(0, pos+1);
			}
			connections.push_back(stoi(line));
			pipes[stoi(token)] = connections;
		}
		myfile.close();
	}
	queue<int> items;
	vector<int> connections;
	int groups = 0;
	/* Here we traverse our pipe structure */
	while (pipes.size() > 0) {
		start = find_min_elem();
		items.push(start);
		while (!items.empty()) {
			current = items.front();
			items.pop();
			if (pipes.find(current) != pipes.end()) {
				connections = pipes.find(current)->second;
				pipes.erase(current);
			}
			for (int a : connections) { 
				/* check if it's already gone to avoid infinite loops */
				if (pipes.find(a) != pipes.end()) { items.push(a); }
			}
		}
		groups++;
	}
	cout << "number of groups: " << groups << endl;
	return 0;
}

int main() {
	part_one();
	return 0;
}