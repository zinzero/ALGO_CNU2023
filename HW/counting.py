num_lst = [1, 4, 1, 2, 7, 5, 2]
print(f"정렬 안 된 리스트 : {num_lst}")


def counting_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)

    for num in arr:
        count[num] += 1

    print(f"카운팅 결과 : {count}")

    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    sorted_arr = [0] * len(arr)

    for num in arr:
        index = count[num] - 1
        sorted_arr[index] = num
        count[num] -= 1
        print(f"카운팅 정렬 중 : {sorted_arr}")

    return sorted_arr


sorted_lst = counting_sort(num_lst)
print(f"카운팅 정렬 후 리스트 : {sorted_lst}")
