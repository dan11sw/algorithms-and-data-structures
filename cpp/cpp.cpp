#include <iostream>
#include <vector>
#include <optional>
#include <cstdint>
using namespace std;

optional<int32_t> binary_search(const vector<int32_t> list, int32_t target) {
	if (list.empty()) {
		return nullopt;
	}

	int32_t low = 0;
	int32_t high = list.size() - 1;

	while (low <= high) {
		int32_t mid = (low + high) / 2;
		int32_t current = list[mid];

		if (current == target) {
			return mid;
		}
		else if (current < target) {
			low = mid + 1;
		}
		else {
			high = mid - 1;
		}
	}

	return nullopt;
}


int main()
{
	vector<int32_t> vec{ 1, 2, 4, 5, 7, 8, 10, 20, 33 };

	optional<int32_t> index = binary_search(vec, 4);

	if (!index.has_value()) {
		cout << "Not found" << endl;
	}
	else {
		cout << "Index: " << index.value() << " Value: " << vec[index.value()] << endl;
	}

	system("PAUSE");
	return 0;
}
