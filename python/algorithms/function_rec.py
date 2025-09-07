from typing import List, Optional

def sum_rec(v_arr: List[int]) -> int:
    if len(v_arr) == 0:
        return 0
    elif len(v_arr) == 1:
        return v_arr[0]

    return v_arr[0] + sum_rec(v_arr[1:])

def len_rec(v_arr) -> int:
    if not isinstance(v_arr, list):
        return 0

    if len(v_arr) == 0:
        return 0

    return 1 + len_rec(v_arr[1:])

def max_item(v_arr: List[int]) -> int:
    if len(v_arr) == 0:
        return 0
    elif len(v_arr) == 1:
        return v_arr[0]

    max_value = v_arr[0]
    new_max_item = max_item(v_arr[1:])

    if max_value < new_max_item:
        max_value = new_max_item

    return max_value

def binary_search_rec(v_arr: List[int], item: int, low=0, high=0) -> Optional[int]:
    if len(v_arr) == 0:
        return None

    if high == 0:
        high = len(v_arr) - 1

    if low <= high:
        mid = (low + high) // 2
        guess = v_arr[mid]

        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1

        return binary_search_rec(v_arr, item, low, high)

    return None


arr = [1, 2, 3, 6, 8, 10, 20, 34]

print(sum_rec(arr))
print(len_rec(arr))
print(max_item(arr))
print()

index = binary_search_rec(arr, 3)
if index:
    print(index, arr[index])