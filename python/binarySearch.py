from quickSort import quick_sort, make_sample_arr


def binary_search(sorted_array: list, target: int, left, right):
    mid: int = (left + right) // 2  # 2로 나눈 몫
    middle_value = sorted_array[mid]

    if left > right:
        return print(f"There are no {target}")

    if target == middle_value:
        return print(f"Index : {mid}")
    elif middle_value > target:
        binary_search(sorted_array, target, left, mid-1)
    elif middle_value < target:
        binary_search(sorted_array, target, mid+1, right)
    else:
        return False


if __name__ == "__main__":
    sample_list = make_sample_arr(100)
    sorted_list = quick_sort(sample_list)

    print(sorted_list)

    left: int = 0  # 첫번째 인덱스
    right: int = len(sorted_list)-1  # 마지막 인덱스
    target: int = 50

    print(f"Target : {target}")

    binary_search(sorted_list, target, left, right)
