#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

enum Action { greater, less, equal, not_equal }; // we get rid of "or equal to by adjusting comp_val"
// typedef struct instruction;
struct INSTRUCTION {
	std::string reg_name;
	int value; 		// we reverse the sign of dec actions
	std::string dependant_reg;
	Action action;
	int comp_val;
}; 

std::vector<INSTRUCTION> process_input() {
	using namespace std;
	string line, token;
	string delimiter = " ";
	int pos, process, val;
	bool inc;
	vector<INSTRUCTION> instructions;
	ifstream myfile ("input.txt");

    if (myfile.is_open()) {
        while (getline (myfile,line)) {
        	process = 0;
        	struct INSTRUCTION inst;
        	while ((pos = line.find(delimiter)) != std::string::npos) {
                token = line.substr(0, pos);
                switch (process) {
                	case 0:
                	    inst.reg_name = token;
                	    break;
                	case 1:
                	    inc = (token.compare("inc") == 0);
                	    break;
                	case 2:
                	    val = stoi(token);
                	    if (!inc) { val = 0 - val; }
                	    inst.value = val;
                	    break;
                	case 4: 
                	    inst.dependant_reg = token;
                	    break;
                	case 5:
                	    val = 0;
                	    if (!token.compare(">")) { inst.action = Action::greater; }
                	    else if (!token.compare("<")) { inst.action = Action::less; }
                	    else if (!token.compare("==")) { inst.action = Action::equal; }
                	    else if (!token.compare("!=")) { inst.action = Action::not_equal; }
                	    else if (!token.compare("<=")) {
                	    	val = 1;
                	    	inst.action = Action::less;
                	    } else {
                	    	val = -1;
                	    	inst.action = Action::greater;
                	    }
                	    break;
                	default:
                	    break;
                }

                process ++;
                line.erase(0, pos + 1);
            }
            // cout << line << "\n";
            val = val + stoi(line);
            inst.comp_val = val;
            cout << inst.reg_name << " depends on " << inst.dependant_reg << " having " << inst.comp_val << "\n";
            instructions.push_back(inst);
        }
        myfile.close();
    }
    return instructions;
}

void part_one() {
	using namespace std;
	vector<INSTRUCTION> instructions;
	map<std::string, int> reg_values;
	bool do_inst;
	int val;
	int max = 0;
	int max_part_two = 0;
	instructions = process_input();

	vector<INSTRUCTION> :: iterator it;
 	for( it = instructions.begin(); it!=instructions.end(); ++it){
    	INSTRUCTION current = *it;
    	if (reg_values.find(current.dependant_reg) == reg_values.end()) {
    		reg_values[current.dependant_reg] = 0;
    	}
    	if (reg_values.find(current.reg_name) == reg_values.end()) {
    		reg_values[current.reg_name] = 0;
    	}

    	switch (current.action){
    		case Action::greater:
    		    do_inst = (reg_values.find(current.dependant_reg)->second > current.comp_val);
    		    break;
    		case Action::less:
    		    do_inst = (reg_values.find(current.dependant_reg)->second < current.comp_val);
    		    break;
    		case Action::equal:
    		    do_inst = (reg_values.find(current.dependant_reg)->second == current.comp_val);
    		    break;
    		case Action::not_equal:
    		    do_inst = (reg_values.find(current.dependant_reg)->second != current.comp_val);
    		    break;
    		default:
    		    cout << "ERROR action unfound\n";
    		    break;
    	}

    	if (do_inst) {
    		val = reg_values.find(current.reg_name)->second + current.value; 
    		reg_values.find(current.reg_name)->second = val;
    		if (val > max_part_two) { max_part_two = val; }
    	}
	}
	for( it = instructions.begin(); it!=instructions.end(); ++it) {
		INSTRUCTION current = *it;
		val = reg_values.find(current.reg_name)->second;
		if (val > max) { max = val; }
	}
	cout << max << " is the max value\n";
	cout << max_part_two << " is the max pt2 value\n";
}

int main() {
	part_one();
	return 0;
}