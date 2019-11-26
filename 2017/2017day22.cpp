#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<string> read_input(){
	ifstream myfile ("input.txt");
	vector<string> graph;
	string line;
	for (int i = 0; i < 500; i++) {
		string row = ".............................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................";
		graph.push_back(row);
	}
	if (myfile.is_open()) {
		while (getline (myfile,line)) {
			string row = "..........................................................................................................................................................................................................................................................";
			row = row + line;
			row = row + "..........................................................................................................................................................................................................................................................";
			graph.push_back(row);
		}
		myfile.close();
	}
	for (int i = 0; i < 500; i++) {
		string row = ".............................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................";
		graph.push_back(row);
	}
	return graph;
}

enum Direction { up, left, down, right };

Direction rotate_virus(int change, Direction current) {
	if (change == 1) {
		return static_cast<Direction>((current+1) % 4);
	} else if (change == 0) {
		if (current == Direction::up) {
			return Direction::right;
		}
		return (static_cast<Direction>(current-1));
	}
	else {
		return static_cast<Direction>((current+2) % 4);
	}
}

void move_forward(int &x, int &y, Direction dir) {
	switch(dir) {
		case Direction::up:
			// cout << "moving up" << endl;
			y--;
			break;
		case Direction::left:
			// cout << "moving left" << endl;
			x--;
			break;
		case Direction::down:
			// cout << "moving down" << endl;
			y++;
			break;
		case Direction::right:
			// cout << "moving right" << endl;
			x++;
			break;
	}
}

void move_virus(vector<string> &graph, int time) {
	int x = 262;
	int y = 512;
	int num_infected = 0;
	Direction current = Direction::up;
	string row;
	for (int t = 0; t < time; t++) {
		row = graph.at(y);
		if (row[x] ==  '#') {
			current = rotate_virus(0, current);
			row = row.substr(0, x) + "F" + row.substr(x+1, string::npos);
		} else if (row[x] == 'W') {
			row = row.substr(0, x) + "#" + row.substr(x+1, string::npos);
			num_infected++;
		} else if (row[x] == 'F') {
			current = rotate_virus(2, current);
			row = row.substr(0, x) + "." + row.substr(x+1, string::npos);
		} else { 	// clean
			current = rotate_virus(1, current);
			row = row.substr(0, x) + "W" + row.substr(x+1, string::npos);
		}
		graph.at(y) = row;
		move_forward(x, y, current);
		if (x < 0 || x > 500) {
			cout << "running off the x-axis: " << x << endl;
		} else if (y < 0 || y > 1024) {
			cout  << "running off the y-axis: " << y << endl;
		}
	}
	cout << "virus infected " << num_infected << endl;
}

int main() {
	vector<string> graph = read_input();
	move_virus(graph, 10000000);
}