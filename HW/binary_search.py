num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(lst, key, low, high):
    if low <= high:
        mid = (low + high) // 2
        if key == lst[mid]:
            return print(f"이진 탐색 결과 : target이 {mid} 위치에 있습니다.")
        elif key < lst[mid]:
            print(f"이진 탐색 중 : 탐색 범위를 {low} ~ {mid -1}로 변경합니다.")
            return binary_search(lst, key, low, mid - 1)
        else:
            print(f"이진 탐색 중 : 탐색 범위를 {mid + 1} ~ {high}로 변경합니다.")
            return binary_search(lst, key, mid + 1, high)
    return print("이진 탐색 결과 : target 찾지 못 했습니다.")


target = 9

binary_search(num_lst, target, 0, len(num_lst) - 1)
