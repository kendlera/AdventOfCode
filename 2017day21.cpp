#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <numeric>

using namespace std;

map<string, string> read_inputs() {
	ifstream myfile ("input.txt");
	string delimiter = " => ";
	string line, input_pattern;
	int pos;
	/* we could optimize for 2x2 vs 3x3 */
	/* could also optimize by number of 'on' pixels */
	map<string, string> transforms;
    if (myfile.is_open()) {
        while (getline (myfile,line)) {
        	pos = line.find(delimiter);
        	input_pattern = line.substr(0, pos);
        	line.erase(0, pos+4);
        	transforms[input_pattern] = line;
        }
        myfile.close();
    }
    return transforms;
}

string get_string_version(vector<string> group) {
	stringstream  ans;
	string delimiter = "/";
	copy(group.begin(),group.end(), ostream_iterator<string>(ans,delimiter.c_str()));
	string result = ans.str();
	result.erase(result.size()-1, 1);
	return result;
}

vector<string> get_vector_version(string pattern) {
	vector<string> vector_version;
	string token;
	int pos;
	string delimiter = "/";
	while ((pos = pattern.find(delimiter)) != string::npos) {
		token = pattern.substr(0, pos);
		pattern.erase(0, pos+1);
		vector_version.push_back(token);
	}
	vector_version.push_back(pattern);
	return vector_version;
}

vector<string> flip_group(vector<string> group) {
	string row;
	vector<string> new_group;
	for (int i = 0; i < group.size(); i++) {
		row = group.at(i);
		reverse(row.begin(), row.end());
		new_group.push_back(row);
	}
	return new_group;
}

vector<string> rotate_group(vector<string> group) {
	vector<string> new_group;
	string row;
	int g_size = group.size()-1;
	for (int i = 0; i <= g_size; i++) {
		row = "";
		for (int j = g_size; j >= 0; j--) {
			row = row + group.at(j)[i];
		}
		new_group.push_back(row);
	}
	return new_group;
}

vector<string> match_rule(map<string, string> &transforms, vector<string> group) {
	vector<string> output, flipped;
	string str_repr;
	for (int rotation = 0; rotation < 4; rotation++) {
		// check if group matches rule
		str_repr = get_string_version(group);
		if (transforms.find(str_repr) != transforms.end()) {
			// cout << "found rule for " << str_repr << endl;
			return get_vector_version(transforms.find(str_repr)->second);
		}
		// check if flipped group matches rule
		flipped = flip_group(group);
		str_repr = get_string_version(flipped);
		if (transforms.find(str_repr) != transforms.end()) {
			// cout << "found rule for " << str_repr << endl;
			return get_vector_version(transforms.find(str_repr)->second);
		}
		// rotate group
		group = rotate_group(group);
	}
	cout << "unable to find rule!" << endl;
	return output;
}

vector<string> manipulate_graph(map<string, string> &transforms, vector<string> graph, int iterations) {
	int x, y; 	// we use these to keep track of the top left coordinate of our group
	string slice;
	vector<string> new_chunk;
	for (int i = 0; i < iterations; i++) {
		cout << "round " << i+1 << endl;
		vector<string> new_graph;
		if (graph.size()%2 == 0) {
			// break into even groups
			for (int row = 0; row < graph.size(); row = row+2) {
				x = row;
				string row0 = "";
				string row1 = "";
				string row2 = "";
				for (int col = 0; col < graph.size(); col = col+2) {
					y = col;
					vector<string> chunk;
					slice = graph.at(x).substr(y, 2);
					chunk.push_back(slice);
					slice = graph.at(x+1).substr(y, 2);
					chunk.push_back(slice);
					new_chunk = match_rule(transforms, chunk);
					row0 = row0 + new_chunk.at(0);
					row1 = row1 + new_chunk.at(1);
					row2 = row2 + new_chunk.at(2);
				}
				new_graph.push_back(row0);
				new_graph.push_back(row1);
				new_graph.push_back(row2);
			}
		} else {
			// break into odd groups
			for (int row = 0; row < graph.size(); row = row+3) {
				x = row;
				string row0 = "";
				string row1 = "";
				string row2 = "";
				string row3 = "";
				for (int col = 0; col < graph.size(); col = col+3) {
					y = col;
					vector<string> chunk;
					slice = graph.at(x).substr(y, 3);
					chunk.push_back(slice);
					slice = graph.at(x+1).substr(y, 3);
					chunk.push_back(slice);
					slice = graph.at(x+2).substr(y, 3);
					chunk.push_back(slice);
					new_chunk = match_rule(transforms, chunk);
					row0 = row0 + new_chunk.at(0);
					row1 = row1 + new_chunk.at(1);
					row2 = row2 + new_chunk.at(2);
					row3 = row3 + new_chunk.at(3);
				}
				new_graph.push_back(row0);
				new_graph.push_back(row1);
				new_graph.push_back(row2);
				new_graph.push_back(row3);
			}
		}
		graph = new_graph;
	}
	return graph;
}

int count_on(vector<string> graph) {
	int ans = 0;
	int pos;
	string on = "#";
	string current;
	for (int i = 0; i < graph.size(); i ++) {
		current = graph.at(i);
		while ((pos = current.find(on)) != string::npos) {
			ans++;
			current.erase(0, pos+1);
		}
	}
	return ans;
}

int main() {
	map<string, string> transforms;
	transforms = read_inputs();
	vector<string> group;
	group.push_back(".#.");
	group.push_back("..#");
	group.push_back("###");
	// this is the initial configuration
	group = manipulate_graph(transforms, group, 18);
	for (string row : group) {
		cout << row << endl;
	}
	cout << "after 18 iterations, there are " << count_on(group) << " pixels on" << endl;
}