#include <iostream>
#include <fstream>
#include <vector>

void part_two() {
	using namespace std;
	string line;
	vector<int> jump_slots;
	ifstream myfile ("input.txt");

    if (myfile.is_open()) {
        while (getline (myfile,line)) {
        	jump_slots.push_back(stoi(line));
        }
        myfile.close();
    }
    // cout << jump_slots.size() << "\n";
    int goal = jump_slots.size();
    int current_pos = 0;
    int steps = 0;
    while(current_pos < goal) {
    	if (jump_slots.at(current_pos) >= 3) {
    		jump_slots.at(current_pos)--;
    		current_pos = current_pos + jump_slots.at(current_pos) + 1;

    	} else {
    		jump_slots.at(current_pos)++;
    		current_pos = current_pos + jump_slots.at(current_pos) - 1;
    	}
    	
    	steps++;
    }
    cout << "took " << steps << "\n";
}


int main() {
	part_one();
	return 0;
}