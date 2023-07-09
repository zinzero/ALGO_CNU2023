num_lst = [4, 8, 2, 6, 1, 9, 5, 7, 3, 10]
print(f"정렬 안 된 리스트 : {num_lst}")


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        print(f"STEP{i} : {arr}")
    return arr


sorted_lst = insertion_sort(num_lst)

print(f"삽입 정렬 후 리스트 : {sorted_lst}")

