# 두 개의 행렬 n X n  행렬을 억지 기법과 쉬트라쏀 알고리즘으로 구현한 프로그램
# 시간복잡도
# 억지 기법 : O(n^3)
# 쉬트라쎈 : O(n^log2(7))
import time  # 프로그램 실행시간을 알아보기 위한 모듈
import numpy as np  # 쉬트라쎈 알고리즘을 풀 때 사용하기 위한 모듈

start_time = time.time()  # 프로그램 시작 시간


# 행렬 곱셈 억지 기법
def multiply(A, B, C):
    for row in range(len(A)):  # 행렬의 행의 길이만큼 -> O(n)
        for col in range(len(B[0])):  # 행렬 B의 열의 길이 만큼 -> O(n)
            for k in range(len(A[0])):  # 행렬 A의 열의 길이 만큼 -> O(n)
                C[row][col] = C[row][col] + A[row][k] * B[k][col]
                # nXn 행렬의 곱을 구하기 위해 반복문을 3번 사용함 -> O(n^3)


# 행렬 곱셈 쉬트라쎈 알고리즘
def strassen(A, B):
    # T(n) = 7T(n/2), T(1) = 1
    n = len(A)  # n X n 행렬의 길이 n
    if n == 1:  # 슬라이싱 해서 파라미터로 입력 받은 행렬의 길이가 1이면
        return A * B  # 곱한 값을 반환

    n2 = n // 2

    # 부분 행렬로 슬라이싱
    A11, A12, A21, A22 = A[:n2, :n2], A[:n2, n2:], A[n2:, :n2], A[n2:, n2:]
    B11, B12, B21, B22 = B[:n2, :n2], B[:n2, n2:], B[n2:, :n2], B[n2:, n2:]

    # 재귀적으로 불러서 값을 반환시킨다
    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    # 전체 행렬 C의 부분 행렬의 값을 넣어준다.
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 + M3 - M2 + M6

    # numpy 함수를 이용하여 부분 행렬을 전체 행렬로 합쳐준다.
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return C


A = []
B = []
C = []

n = int(input())  # nXn 행렬의 크기

# 행렬의 값을 입력 받음
for _ in range(n):
    a, b = map(int, input().split())
    A.append([a, b])

for _ in range(n):
    a, b = map(int, input().split())
    B.append([a, b])

# C 행렬은 0으로 초기화
for _ in range(n):
    C.append([0] * n)

# 쉬트라쎈 알고리즘을 풀기 위해 numpy 행렬로 변환
np_A = np.array(A)
np_B = np.array(B)

end_time = time.time()  # 프로그램 종료 시간

print("실행시간 : ", end_time - start_time)  # 프로그램 실행시간 출력
multiply(A, B, C)  # 억지기법 행렬 곱 계산
print("multiply : ")
print(C)
print()
print("strassen : ")
print(strassen(np_A, np_B))  # 쉬트라쎈 알고리즘 행렬 곱 계산


