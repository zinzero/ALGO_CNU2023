num_lst = [4, 8, 2, 6, 1, 9, 5, 7, 3, 10]


def linear_search(arr, target):
    n = len(arr)

    for i in range(n):
        if arr[i] == target:
            return print(f"선형 탐색 결과 : {i}번째의 target이 있습니다.")
        else:
            print(f"선형 탐색 중 : {i}번째의 target이 없습니다.")

    return print(f"선형 탐색 결과 : target을 찾을 수 없습니다.")


target = 6

linear_search(num_lst, target)
