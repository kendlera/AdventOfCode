#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <cstdlib>
#include <thread>
#include <mutex>
#include <unistd.h> // sleep

using namespace std;
mutex mu;

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

vector<int> execute_program_pt_one( vector<string> &instructions, map<string, long long> &registers, int &current_line, vector<int> &my_msgs) {
	// long long current_line = start_line;
	int pos;
	long long op1int, op2int, op, last_sound;
	vector<int> sent_msgs;
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
		// cout << current_line << " " << line << endl;
		pos = line.find(separator);
		command = line.substr(0, pos);
		line.erase(0, pos+1);
		if (!command.compare("snd")) {
			op = get_value(registers, line);
			cout << "sending " << op << endl;
			// last_sound = op;
			sent_msgs.push_back(op);
			current_line++;
		} else if (!command.compare("set")) {
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
			current_line++;
		} else if (!command.compare("mod")) {
			// modulo
			pos = line.find(separator);
			op1 = line.substr(0, pos);
			if (registers.find(op1) == registers.end()) { registers[op1] = 0; }
			op2str = line.substr(pos+1, string::npos);
			op = get_value(registers, op2str);
			// cout << op1 << " becomes " << registers[op1]  << " % " << op << endl;
			registers[op1] = registers[op1] % op;
			current_line++;
		} else if (!command.compare("rcv")) {
			// recover
			if (my_msgs.size() == 0) {
				return sent_msgs;
			} else {
				op = my_msgs.at(0);
				my_msgs.erase(my_msgs.begin());
				cout << "received msg to store " << op << " in " << line << endl;
				registers[line] = op;
			}
			/* if (registers.find(line) == registers.end()) { registers[line] = 0; }
			cout << "checking if " << line << ": " << registers[line] << " == 0"  << endl;
			if (registers[line] != 0) {
				cout << "recovered frequency " << last_sound << endl;
				return;
			} */
			current_line++;
		} else {
			// jump if greater than 0
			pos = line.find(separator);
			op1 = line.substr(0, pos);
			op1int = get_value(registers, op1);
			op2str = line.substr(pos+1, string::npos);
			op = get_value(registers, op2str);
			// cout << "jump " << op << " if " << op1 << ": " << registers[op1] << " > 0" << endl;
			if (op1int > 0) {
				current_line = current_line + op;
			} else {
				current_line++;
			}
		}
	}
	cout << "finished executing all instructions" << endl;
	return sent_msgs;
}
void execute_program_pt_two(vector<string> instructions) {
	vector<int> msgs;
	bool done = false;
	int num_sent = 0;
	int curr_running = 0;
	map<string, long long> registers0;
	registers0["p"] = 0;
	map<string, long long> registers1;
	registers1["p"] = 1;
	int curr_line0 = 0;
	int curr_line1 = 0;
	int consecutive_zeros = 0;
	while(!done) {
		if (curr_running == 0) {
			cout << "sending " << msgs.size() << " messages to program 0; resuming it at line " << curr_line0 << endl;
			msgs = execute_program_pt_one(instructions, registers0, curr_line0, msgs);
		} else {
			cout << "sending " << msgs.size() << " messages to program 1; resuming it at line " << curr_line1 << endl;
			msgs = execute_program_pt_one(instructions, registers1, curr_line1, msgs);
			num_sent = num_sent + msgs.size();
		}
		if (msgs.size() == 0) {
			consecutive_zeros++;
			if (consecutive_zeros > 2) { 
				cout << num_sent << " messages sent by program 1" << endl; 
				return;
			}
		} else {
			consecutive_zeros = 0;
		}
		curr_running = 1 - curr_running;
	}

}

void run_instructions() {
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
    // execute_program_pt_one(instructions);


    execute_program_pt_two(instructions);
}

int main() {
	run_instructions();
}