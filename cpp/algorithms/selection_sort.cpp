#include <iostream>
#include <vector>
#include <optional>
#include <cstdint>
using namespace std;

optional<std::int32_t> find_smallest(const vector<int32_t>& arr) {
	if (arr.empty()) {
		return nullopt;
	}

	int32_t smallest = arr[0];
	int32_t index = 0;

	for (int32_t i = 1; i < arr.size(); i++) {
		int32_t item = arr[i];
		if (item < smallest) {
			smallest = item;
			index = i;
		}
	}

	return index;
}

vector<int32_t> selection_sort(const vector<int32_t>& arr) {
	if (arr.empty()) {
		return arr;
	}

	vector<int32_t> old_arr{ arr };
	vector<int32_t> new_arr;
	new_arr.reserve(old_arr.size());

	const int32_t size = old_arr.size();
	for (int32_t i = 0; i < size; i++) {
		optional<int32_t> index = find_smallest(old_arr);
		if (index.has_value()) {
			new_arr.push_back(old_arr[index.value()]);
			old_arr.erase(old_arr.begin() + index.value());
		}
	}

	return new_arr;
}

int main()
{
	vector<int32_t> vec{ 1, 2, 3, -100, -123, -5, 34, 23, 100 };
	vector<int32_t> new_vec = selection_sort(vec);

	for (const auto& item : new_vec) {
		cout << item << " ";
	}

	cout << endl;

	system("PAUSE");
	return 0;
}
