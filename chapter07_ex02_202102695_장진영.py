# LCS 테이블에서 LCS를 추적하는 알고리즘을 구현한 프로그램
# 시간복잡도 : O(mn)
# m : 문자열1의 길이
# n : 문자열2의 길이
import time  # 프로그램 실행시간을 알아보기 위한 모듈

start_time = time.time()  # 프로그램 시작 시간


def lcs_dp(X, Y):
    m = len(X)  # X 문자열의 길이
    n = len(Y)  # Y 문자열의 길이
    L = [[None] * (n + 1) for _ in range(m + 1)]  # LCS 테이블 생성

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                # 첫 번째 행과 열은 0으로 초기화
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                # 현재 문자가 같은 경우, 이전 대각선에서의 LCS 값에 1을 더해 저장
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                # 현재 문자가 다른 경우, 이전 행 또는 열에서의  LCS 값 중 큰 값을 선택
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    print("LCS =", lcs_dp_traceback(X, Y, L))  # lcs_dp_traceback() 함수를 호출

    return L[m][n]


def lcs_dp_traceback(X, Y, L):
    lcs = ""  # lcs를 저장하는 변수
    i = len(X)  # X 문자열의 길이
    j = len(Y)  # Y 문자열의 길이

    # LCS 테이블을 역추적하며 실제 LCS 값을 찾는다.
    while i > 0 and j > 0:
        v = L[i][j]  # 현재 LCS 테이블의 값

        if v == L[i][j - 1]:
            # 현재 열의 값이 이전 열의 값과 같은 경우
            # 왼쪽으로 이동하여 다음 열을 비교
            j -= 1
        elif v == L[i - 1][j]:
            # 현재 행의 값이 이전 행의 값과 같은 경우
            # 위로 이동하여 다음 행을 비교
            i -= 1
        else:
            # 현재 행과 열의 값이 다른 경우, 대각선 방향으로 이동하여 실제 문자를 찾는다.
            i -= 1
            j -= 1
            lcs = X[i] + lcs  # 찾은 문자를 LCS에 추가한다.

    return lcs


X = input().strip()  # X 문자열 입력
Y = input().strip()  # Y 문자열 입력


end_time = time.time()  # 프로그램 종료 시간

print("실행시간 : ", end_time - start_time)  # 프로그램 실행시간 출력
print("X =", X)  # 첫번째 문자열 출력
print("Y =", Y)  # 두번째 문자열 출력
lcs_dp(X, Y)  # 문자열 비교 실행
