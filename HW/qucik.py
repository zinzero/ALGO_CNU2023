num_lst = [4, 8, 2, 6, 1, 9, 5, 7, 3, 10]
print(f"정렬 안 된 리스트 : {num_lst}")


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left, equal, right = [], [], []
    print(f"pivot : {pivot}")

    for num in arr:
        if num < pivot:
            left.append(num)
            print(f"left : {left}")
        elif num == pivot:
            equal.append(num)
            print(f"equal : {equal}")
        else:
            right.append(num)
            print(f"right : {right}")

    return quick_sort(left) + equal + quick_sort(right)


sorted_lst = quick_sort(num_lst)
print(f"퀵 정렬 후 리스트 : {sorted_lst}")
