#include <iostream>
#include <fstream>
#include <string>
#include <set>

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

int main() {
	part_one();
	return 0;
}