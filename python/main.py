from typing import List, Optional

def binary_search(arr: List[int], item: int) -> Optional[int]:
    if not isinstance(arr, list):
        print("For binary search need list")
        return None

    if len(arr) == 0:
        return None

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1

    return None


if __name__ == "__main__":
    test_list = [1, 2, 4, 5, 6, 7]

    index = binary_search(test_list, 3)
    print(index)

    if index is not None:
        print(test_list[index])




