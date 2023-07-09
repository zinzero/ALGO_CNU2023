num_lst = [4, 8, 2, 6, 10, 1, 9, 5, 7, 3]
print(f"정렬 안 된 리스트 : {num_lst}")


def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        print(f"쉘 정렬 중 : {arr}")
        gap //= 2

    return arr


sorted_lst = shell_sort(num_lst)
print(f"쉘 정렬 후 리스트 : {sorted_lst}")
