num_lst = [3790, 2850, 5162, 4122, 1043, 6894, 5425, 2706, 2267, 1679]
print(f"정렬 안 된 리스트 : {num_lst}")


def radix_sort(arr):
    max_value = max(arr)
    max_digit = len(str(max_value))

    for digit in range(max_digit):
        arr = counting_sort(arr, digit)
        print(f"STEP {digit + 1} : {arr}")

    return arr


def counting_sort(arr, digit):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // 10 ** digit) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // 10 ** digit) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

    return arr


sorted_lst = radix_sort(num_lst)
print(f"기수 정렬 후 리스트 : {sorted_lst}")