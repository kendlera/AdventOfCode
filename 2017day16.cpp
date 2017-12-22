#include <iostream>
#include <fstream>
#include <string>
#include <set>

using namespace std; 

string dance_move(string programs, string command) {
	string slash = "/";
	int pos, swap1, swap2;
	string type, token;
	char saved;
	type = command.substr(0, 1);
	command.erase(0, 1);
	if (!type.compare("s")) {
		for (int i = 0; i < stoi(command); i++) {
			token = programs[15];
			programs.erase(15, 1);
			programs = token + programs;
		}
	} 
	else {
		pos = command.find(slash);
		if (!type.compare("p")) {
			// swap based on letter
			token = command.substr(0, pos);
			command.erase(0, pos+1);
			swap1 = programs.find(token);
			swap2 = programs.find(command);
		} else {
			// swap based on position
			swap1 = stoi(command.substr(0, pos));
			command.erase(0, pos+1);
			swap2 = stoi(command);
		}
		saved = programs[swap1];
		programs[swap1] = programs[swap2];
		programs[swap2] = saved;
	}
	return programs;
}

void part_one() {
	ifstream inFile;
	string input, command, input_cpy;
	inFile.open("input.txt");
	inFile >> input;
	int pos;
	int counter = 0;
	string comma = ",";
	string programs = "abcdefghijklmnop";
	set<string> all_combos;
	all_combos.insert(programs);
	for (int i = 0; i < 1000000000 % 36; i++) { // we loop to the start every 35 iterations
		input_cpy = input;
		while ((pos = input_cpy.find(comma)) != string::npos) {
			// cout << programs << endl;
			command = input_cpy.substr(0, pos);
			// cout << command << endl;
			input_cpy.erase(0, pos+1);
			programs = dance_move(programs, command);
		}
		programs = dance_move(programs, input_cpy);
		cout << programs << endl;
		/* all_combos.insert(programs);
		if (all_combos.size() < i+1) { 
			cout << i << " completed a loop";
			return;
		} */
	}
}

int main() {
	part_one();
	return 0;
}