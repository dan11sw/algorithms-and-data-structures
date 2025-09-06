from typing import List, Optional


def find_smallest(f_arr: List[int]) -> Optional[int]:
    if len(f_arr) == 0:
        return None

    smallest = f_arr[0]
    smallest_index = 0

    for i in range(1, len(f_arr)):
        item = f_arr[i]

        if item < smallest:
            smallest = item
            smallest_index = i

    return smallest_index

def selection_sort(f_arr: List[int]) -> List[int]:
    if len(f_arr) == 0:
        return f_arr

    l_arr = []
    for i in range(len(f_arr)):
        smallest = find_smallest(f_arr)
        if smallest is not None:
            l_arr.append(f_arr.pop(smallest))

    return l_arr


if __name__ == "__main__":
    arr = [1, 2, -12, 3, 4, 100, -23]

    index = find_smallest(arr)
    if index is not None:
        print("Index: ", index, " Value: ", arr[index])

    new_arr = selection_sort(arr)
    print(new_arr)
    print(arr)






