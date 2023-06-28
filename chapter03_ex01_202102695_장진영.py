# 문자열 매칭 알고리즘을 구현한 프로그램
# 입력받은 문자에 대해 패턴 문자열과 일치하는 부분을 찾는다.
# 시간복잡도 : O(mn)
import time

start = time.time()


def string_matching(T, P):
    n = len(T)  # T 문자열 길이
    m = len(P)  # P 문자열 길이
    for i in range(n - m + 1):  # 반복문 T(n - m + 1) -> 상수는 무의미 T(n)
        j = 0
        # j가 비교하는 문자열의 길이 보다 크면 안 됨.
        # T의 문자와 P의 문자가 일치하는지 판단
        while j < m and P[j] == T[i + j]:  # 패턴 문자열 만큼 비교 T(m)
            j = j + 1
        if j == m:  # P의 문자와 T의 문자가 모두 일치할 때
            return i  # 일치하는 시작 위치를 반환
    return -1  # 매칭 되는 문자열이 없을 경우 -1 반환


end = time.time()
T = input()  # 입력 문자열
P = input()  # 패턴 문자열

print("실행시간 : ", end - start)
print(string_matching(T, P))  # 결과 출력
