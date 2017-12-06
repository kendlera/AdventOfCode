#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <vector>
#include <iterator>
#include <set>

void part_two(std::set<std::string> states, std::string target);

void part_one() {
	using namespace std;
	string line;
	char *token;
	int current;
	vector<int> registers;
	ifstream myfile ("input.txt");

    if (myfile.is_open()) {
        while (getline (myfile,line)) {
        	char *cstr = new char[line.length() + 1];
        	strcpy(cstr, line.c_str());
        	token = strtok (cstr, "\t");
            while (token != NULL) {
            	cout << "register: " << token << "\n";
            	current = atoi(token);
            	registers.push_back(current);
            	token = strtok (NULL, "\t");
            }
        }
        myfile.close();
    }
    int num_registers = registers.size();
    cout << num_registers << " registers ready\n";
    string target = "1 0 14 14 12 12 10 10 8 8 6 6 4 3 2 1 ";
    int cycles = 0;
    std::vector<int>::iterator max;
    set<string> states;
    int index, distribute;
    bool found = false;
    const char *delim = " ";
    while (!found) {
    	max = max_element(registers.begin(), registers.end());
    	index = std::distance(registers.begin(), max);
    	// index = registers.find(max);
    	distribute = registers.at(index);
    	registers.at(index) = 0;
    	for (int i = 0; i < distribute; i++) {
    		index = (index + 1) % num_registers;
    		registers.at(index)++;
    	}
    	std::stringstream result;
		std::copy(registers.begin(), registers.end(), std::ostream_iterator<int>(result, " "));
		if (result.str().compare(target) == 0) {
			cout << "match at " << cycles << "\n";
		}
		states.insert(result.str());
		if (cycles == states.size()) {
			cout << "cycles " << cycles + 1 << "\n";
			return;
		} 
		cycles ++;
    }
}


int main() {
	part_one();
	return 0;
}