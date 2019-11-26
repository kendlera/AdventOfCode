#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <cmath>


using namespace std;

int get_distance(float x, float y) {
	int col_axis_distance = floor(abs(x)/2);
	if (y == floor(abs(y)) + .5){
		y = floor(abs(y)) - 1;
	}
	if (y <= col_axis_distance) { return x; }
	return abs(x) + y - col_axis_distance;
}

int part_one() {
	ifstream inFile;
	string input;
	/* learning new ways to read from files! */
	inFile.open("input.txt");
	inFile >> input;

	string delimiter = ",";
	string token;
	int pos, current;
	float x = 0;
	float y = 0;
	int max = 0;
	while ((pos = input.find(delimiter)) != std::string::npos) {
		token = input.substr(0, pos);
		if (!token.compare("n")) {
			y++;
		} else if (!token.compare("nw")) {
			y = y + .5;
			x--;
		} else if (!token.compare("sw")) {
			y = y - .5;
			x--;
		} else if (!token.compare("s")) {
			y--;
		} else if (!token.compare("se")) {
			y = y - .5;
			x++;
		} else {
			y = y + .5;
			x++;
		}
		input.erase(0, pos + 1);
		current = get_distance(x, y);
		if (current > max) { max = current; }
	}
	cout << x << ", " << y << endl;
	cout << "max distance: " << max << endl;
	return get_distance(x, y);
}

int main() {
	int ans = part_one();
	cout << "total distance: " << ans << endl;
	return 0;
}