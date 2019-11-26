#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>

using namespace std;

long long get_value(map<string, long long> &regs, string op) {
	long long digit = atoi(op.c_str());
	if (digit != 0 || !op.compare("0")) { 				// if it's a digit
		return digit;
	}
	if (regs.find(op) == regs.end()) { 
		regs[op] = 0; 									// if it's not present in the register
		return 0; 
	} 	
	return regs[op]; 									// if present in registers
}

void show_registers(map<string, long long> &registers) {
	map<string, long long>::iterator it;
	for (it = registers.begin(); it != registers.end(); it++) {
		cout << it->first << " : " << it->second << endl;
	}
	cout << "\n\n" << endl;
}

void execute(vector<string> &instructions) {
	int pos;
	int current_line = 0;
	int num_muls = 0;
	long long op1int, op2int, op, last_sound;
	map<string, long long> registers;
	registers["a"] = 1;
	string separator = " ";
	string line, command, op1, op2str, cont;
	bool done = false;
	cout << "executing instructions" << endl;
	while (!done) {
		// cin >> cont;
		if (current_line >= instructions.size()) {
			done = true;
			break;
		}
		line = instructions[current_line];
		pos = line.find(separator);
		command = line.substr(0, pos);
		line.erase(0, pos+1);
		if (!command.compare("set")) {
			// set
			pos = line.find(separator);
			op1 = line.substr(0, pos);
			if (registers.find(op1) == registers.end()) { registers[op1] = 0; }
			op2str = line.substr(pos+1, string::npos);
			op = get_value(registers, op2str);
			// cout << op1 << " becomes " << op << endl;
			registers[op1] = op;
			current_line++;
		} else if (!command.compare("add")) {
			// add
			pos = line.find(separator);
			op1 = line.substr(0, pos);
			if (registers.find(op1) == registers.end()) { registers[op1] = 0; }
			op2str = line.substr(pos+1, string::npos);
			op = get_value(registers, op2str);
			// cout << op1 << " becomes " << registers[op1]  << " + " << op << endl;
			registers[op1] = (registers[op1] + op);
			current_line++;
		} else if (!command.compare("mul")) {
			// multiply
			pos = line.find(separator);
			op1 = line.substr(0, pos);
			if (registers.find(op1) == registers.end()) { registers[op1] = 0; }
			// cout << op1 << " becomes " << registers[op1]  << " x " << line.substr(pos+1, string::npos) << endl;
			op2str = line.substr(pos+1, string::npos);
			op = get_value(registers, op2str);
			registers[op1] = (registers[op1] * op);
			num_muls++;
			current_line++;
		} else if (!command.compare("sub")) {
			// modulo
			pos = line.find(separator);
			op1 = line.substr(0, pos);
			if (registers.find(op1) == registers.end()) { registers[op1] = 0; }
			op2str = line.substr(pos+1, string::npos);
			op = get_value(registers, op2str);
			// cout << op1 << " becomes " << registers[op1]  << " % " << op << endl;
			registers[op1] = registers[op1] - op;
			current_line++;
		} else {
			// jump if not 0
			if (registers["h"] != 0) {
				cout << "instruction " << current_line << endl;
				show_registers(registers);
			}
			pos = line.find(separator);
			op1 = line.substr(0, pos);
			op1int = get_value(registers, op1);
			op2str = line.substr(pos+1, string::npos);
			op = get_value(registers, op2str);
			// cout << "jump " << op << " if " << op1 << ": " << registers[op1] << " > 0" << endl;
			if (op1int != 0) {
				current_line = current_line + op;
			} else {
				current_line++;
			}
		}
	}
	cout << "finished executing all instructions" << endl;
	// cout << num_muls << " multiplication instructions" << endl;
	cout << registers["h"] << " is the final value of register h" << endl;
}

int main() {
	ifstream myfile ("input.txt");
	string input, line;
	cout << "opening file" << endl;
	vector<string> instructions;
    if (myfile.is_open()) {
        while (getline (myfile,line)) {
        	instructions.push_back(line);
        }
        myfile.close();
    }
	execute(instructions);
}