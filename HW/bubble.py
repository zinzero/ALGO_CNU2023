def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


num_lst = [4, 8, 2, 6, 1, 9, 5, 7, 3, 10]

print(f"정렬 전 리스트 : {num_lst}")
print(f"버블 정렬 후 리스트 : {bubble_sort(num_lst)}")
