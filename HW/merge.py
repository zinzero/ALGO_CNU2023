num_lst = [4, 8, 2, 6, 1, 9, 5, 7, 3, 10]
print(f"정렬 안 된 리스트 : {num_lst}")


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    print(f"left : {left}")
    print(f"right : {right}")

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


sorted_lst = merge_sort(num_lst)

print(f"병합 정렬 후 리스트 : {sorted_lst}")
