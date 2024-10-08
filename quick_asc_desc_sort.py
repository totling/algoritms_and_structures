from random import randint, sample
from datetime import datetime

start_time = datetime.now()


def quick_ascending_sort(array):
    len_array = len(array)
    if len_array < 2:
        return array
    else:

        supp_elem = array[randint(0, len_array - 1)]
        less = [i for i in array if i < supp_elem]
        greater = [i for i in array if i > supp_elem]

        return quick_ascending_sort(less) + [supp_elem] + quick_ascending_sort(greater)


def quick_descending_sort(array):
    len_array = len(array)
    if len_array < 2:
        return array
    if len_array == 2:
        return [array[0], array[1]] if array[0] > array[1] else [array[1], array[0]]

    supp_elem = array[randint(0, len_array - 1)]
    less = [i for i in array if i < supp_elem]
    greater = [i for i in array if i > supp_elem]

    return quick_descending_sort(greater) + [supp_elem] + quick_descending_sort(less)


arr = sample(range(1, 100000001), 10000000)
print(sorted(arr))
# print(quick_descending_sort(arr))
end_time = datetime.now()

execution_time = end_time - start_time
print(f"Время выполнения программы: {execution_time}")
