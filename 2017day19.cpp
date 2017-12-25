#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

enum Direction { up, down, left, right };

Direction pivot(vector<string> our_map, int x, int y, Direction previous) {
	/* we call this when we encounter a '+' */
	string row = our_map.at(y);
	if (row.at(x-1) != ' ' && previous != Direction::right) {
		return Direction::left;
	} else if (row.at(x+1) != ' ' && previous != Direction::left) {
		return Direction::right;
	}
	row = our_map.at(y-1);
	if (row.at(x) != ' ' && previous != down) {
		return Direction::up;
	}
	return Direction::down;
}

void traverse_path(vector<string> our_map) {
	bool finished = false;
	int x = 39;
	int y = 0;
	int max_y = our_map.size();
	int max_x;
	int num_steps = 0;
	string row;
	char path_marker;
	Direction current = down;
	while (!finished) {
		switch (current) {
			case Direction::up:
				if (y-1 < 0) { 
					finished = true;
					break; 
				}
				row = our_map.at(y - 1);
				path_marker = row.at(x);
				y--;
				break;
			case Direction::down:
				if (y+1 == max_y) { 
					finished = true;
					break; 
				}
				row = our_map.at(y + 1);
				path_marker = row.at(x);
				y++;
				break;
			case Direction::left:
				if (x-1 < 0) {
					finished = true;
					break;
				}
				row = our_map.at(y);
				path_marker = row.at(x - 1);
				x--; 
				break;
			case Direction::right:
				row = our_map.at(y);
				max_x = row.size();
				if (x+1 == max_x) { 
					finished = true; 
					break;
				}
				path_marker = row.at(x + 1);
				x++;
				break;
		}
		if (path_marker == '+') {
			current = pivot(our_map, x, y, current);
		} else if (path_marker != '|' && path_marker != '-' && path_marker != ' ') {
			cout << path_marker;
		} else if (path_marker == ' ') {
			finished = true;
		}
		num_steps++;
	}
	cout << endl;
	cout << "taken " << num_steps << " steps" << endl;
}

vector<string> build_map() {
	ifstream myfile ("input.txt");
	int pos;
	string line;
	/* each elem in vector is a row at position */
	vector<string> our_map; 
    if (myfile.is_open()) {
        while (getline (myfile,line)) {
        	our_map.push_back(line);
        }
        myfile.close();
    }
    return our_map;
}

int main() {
	vector<string> our_map = build_map();
	traverse_path(our_map);
	// 31398 too high
	return 0;
}