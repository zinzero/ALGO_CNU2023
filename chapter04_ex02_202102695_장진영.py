# 이진탐색 알고리즘을 순환구조(재귀), 반복문으로 구현한 프로그램
# 시간 복잡도 : O(log n)
import time  # 프로그램 실행시간을 알아보기 위한 모듈

start_time = time.time()  # 프로그램 시작 시간


# 이진탐색 알고리즘을 순환구조(재귀)로 구현한 함수
def binary_search(A, key, low, high):
    if low <= high:  # 시작 인덱스가 끝 인덱스 보다 커지지 않게
        mid = (low + high) // 2  # 리스트의 중간 값 인덱스
        if key == A[mid]:  # 리스트의 중간 값과 key의 값이 같다면
            return mid  # 중간값을 반환
        elif key < A[mid]:  # key의 값이 중간 값보다 작은 경우 범위를 앞쪽으로 줄이기
            return binary_search(A, key, low, mid - 1)  # 호출 되면서 범위가 절반으로 줄어들기 때문에 O(log n)
        else:  # key의 값이 중간 값보다 큰 경우 범위를 뒤쪽으로 줄이기
            return binary_search(A, key, mid + 1, high)
    return -1  # key의 값을 찾지 못하면 -1을 반환


# 이진탐색 알고리즘을 반복문으로 구현한 함수
def binary_search_iter(A, key, low, high):
    while low <= high:  # 시작 인덱스가 끝 인덱스 보다 커지지 않을 동안 반복
        mid = (low + high) // 2  # 리스트의 중간 값 인덱스
        if key == A[mid]:  # 리스트의 중간 값과 key의 값이 같다면
            return mid  # mid 값을 반환
        elif key > A[mid]:  # key 값이 중간 값보다 큰 경우
            low = mid + 1  # low의 값을 mid + 1 로 전체 범위를 줄인다. -> 범위가 절반으로 줄어든다 O(log n)
        else:  # key 값이 중간 값보다 작은 경우
            high = mid - 1  # high의 값을 mid - 1 범위를 줄인다.
    return -1  # key의 값을 찾지 못하면 -1을 반환


listA = list(map(int, input().split()))  # 리스트를 입력 받아서 저장한다.
key = int(input())  # 찾기 위한 key

end_time = time.time()  # 프로그램 종료 시간
print("실행시간 : ", end_time - start_time)  # 프로그램 실행시간 출력
print()
print("입력 리스트 =", listA)
print("%d 탐색(순환) -->" % key, binary_search(listA, key, 0, len(listA) - 1))  # 순환구조 이진탐색 출력
print()
print("입력 리스트 =", listA)
print("%d 탐색(반복) -->" % key, binary_search_iter(listA, key, 0, len(listA)-1))  # 반복문 이진탐색 출력
