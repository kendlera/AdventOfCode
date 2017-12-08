#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>

int balance_tree(std::string root, std::map<std::string, int> program_weights, std::map<std::string, std::vector<std::string> > supports);

void part_one() {
	using namespace std;
    string line;
    string paren = "(";
    string delimiter = "->";
    string comma = ",";
    set<string> supported;
    set<string> supporters;
    set<string> root;
    int pos;
    ifstream myfile ("input.txt");

    if (myfile.is_open()) {
        while (getline (myfile,line)) {
        	pos = 0;
            std::string token;
            std::string others;
            while ((pos = line.find(delimiter)) != std::string::npos) { // we dont care about strictly supported disks
            	others = line.substr(pos+2, line.size());
            	pos = line.find(paren);
            	token = line.substr(0, pos-1);
            	supporters.insert(token);
            	cout << token << " supports " << others << "\n";
            	while ((pos = others.find(comma)) != std::string::npos) {
            		token = others.substr(1, pos-1);
            		cout << "adding " << token << "\n";
            		supported.insert(token);
            		others.erase(0, pos+1);
            	}
            	token = others.substr(1, others.size());
            	cout << "adding " << token << "\n";
            	supported.insert(token);
            	break;
            }
        }
        myfile.close();
    }
    // return;
    cout << supporters.size() << " supporters; " << supported.size() << " supported\n";
    std::set_difference(supporters.begin(), supporters.end(), supported.begin(), supported.end(), std::inserter(root, root.end()));

    set<string>:: iterator it;
 	for( it = root.begin(); it!=root.end(); ++it){
    	string ans = *it;
    	cout << "Root: " << ans << endl;
	}
}

int balance_tree(std::string root, std::map<std::string, int> program_weights, std::map<std::string, std::vector<std::string> > supports) {
    using namespace std;
    if (supports.find(root) == supports.end()) { // if there are no disks on top of this disk
        return program_weights.find(root)->second;
    }
    vector<string> disks = supports.find(root)->second;
    set<int> weights;
    int sum = 0;
    int weight;
    for(std::vector<string>::iterator it = disks.begin(); it != disks.end(); ++it) {
        /* std::cout << *it; ... */
        weight = balance_tree(*it, program_weights, supports);
        weights.insert(weight);
        sum = sum + weight;
    }
    if (weights.size() > 1) {
        cout << "Unbalanced! " << root << " with " << sum << "\n";
    }
    return sum + program_weights.find(root)->second;
}

void part_two() {
    using namespace std;
    map<string, int> program_weights;
    map<string, vector<string> > supports;
    map<char,int>::iterator it;
    int l_pos, r_pos, pos, current;
    string l_paren = "(";
    string r_paren = ")";
    string arrow = "->";
    string comma = ",";
    string line;

    ifstream myfile ("input.txt");

    if (myfile.is_open()) {
        while (getline (myfile,line)) {
            std::string program_name;
            std::string token;
            std::string weight;
            std::string others;

            l_pos = line.find(l_paren);
            program_name = line.substr(0, l_pos-1);
            r_pos = line.find(r_paren);
            weight = line.substr(l_pos+1, r_pos - l_pos-1);
            current = stoi(weight);
            /* map the program to its weight */
            program_weights[program_name] = current;

            if ((pos = line.find(arrow)) != std::string::npos) {
                others = line.substr(pos+2, line.size());
                // cout << "supported " << others << "\n";
                vector<string> supported;
                while ((pos = others.find(comma)) != std::string::npos) {
                    token = others.substr(1, pos-1);
                    // cout << "adding " << token << "\n";
                    supported.push_back(token);
                    others.erase(0, pos+1);
                }
                token = others.substr(1, others.size());
                // cout << "adding " << token << "\n";
                supported.push_back(token);
                /* map program to who it supports */
                supports[program_name] = supported;
            }
        }
        myfile.close();
    }
    int total = balance_tree(root, program_weights, supports);
}

int main() {
	part_one();
    part_two();
	return 0;
}