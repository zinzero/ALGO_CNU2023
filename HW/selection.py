num_lst = [4, 8, 2, 6, 1, 9, 5, 7, 3, 10]
print(f"정렬 안 된 리스트 : {num_lst}")


def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"STEP {i + 1} : {arr}")

    return arr


sorted_lst = selection_sort(num_lst)
print(f"선택 정렬 후 리스트 : {sorted_lst}")
