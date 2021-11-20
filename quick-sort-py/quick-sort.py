import random
import time


def quick_sort(target_array: list):
    if len(target_array) <= 1:
        return target_array

    pivot: int = target_array[len(target_array) // 2]

    smaller_arr: list = []
    larger_arr: list = []
    equal_arr: list = []

    for item in target_array:
        if item < pivot:
            smaller_arr.append(item)
        elif item > pivot:
            larger_arr.append(item)
        elif item == pivot:
            equal_arr.append(item)
        else:
            return print(f"\"{item}\" is not a int variable")

    return quick_sort(smaller_arr) + equal_arr + quick_sort(larger_arr)


def make_sample_arr(size: int, start: int = 0, end: int = 100):
    result: list = []

    for i in range(size):
        result.append(random.randint(start, end))

    return result


if __name__ == '__main__':
    # Make random array
    sample_list = make_sample_arr(100)
    print(f"정렬 전: {sample_list}")

    # Normal case
    start_normal_case = time.time()
    sorted_list = quick_sort(sample_list)

    print(f"정렬 후 : {sorted_list}")
    print(f"Normal case L/T : {time.time()-start_normal_case}")

    # Worst case
    start_worst_case = time.time()
    worst_list = quick_sort(sorted_list)

    print(f"최악의 경우 : {worst_list}")
    print(f"Worst case L/T : {time.time()-start_worst_case}")
