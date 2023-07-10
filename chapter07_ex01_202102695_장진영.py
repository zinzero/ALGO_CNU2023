# 배낭 채우기 알고리즘을 분할 정복 방식과 동적 계획법 방식으로 구현한 프로그램
# 분할 정복 시간복잡도 : O(2^n)
# 동적 계획법 시간복잡도 : O(nW)
import time  # 프로그램 실행시간을 알아보기 위한 모듈

start_time = time.time()  # 프로그램 시작 시간


# 분할 정복 방식
def knapSack_dc(W, wt, val, n):
    # 기반 상황 : 가방 용량이 0이거나 아이템이 없는 경우, 가치는 0이므로 0을 반환한다.
    if n == 0 or W == 0:
        return 0

    # 현재 아이템의 무게가 가방 용량을 초과하는 경우,
    if wt[n - 1] > W:
        return knapSack_dc(W, wt, val, n - 1)  # 해당 아이템을 선택 할 수 없으므로 이전 아이템을 재귀 호출
    else:  # 현재 아이템을 선택하는 경우의 가치이
        # 현재 아이템의 가치와 해당 아이템의 무게를 뺀 가방 용량으로 재귀 호출하여 계산한다.
        valWithout = knapSack_dc(W, wt, val, n - 1)
        valWith = val[n - 1] + knapSack_dc(W-wt[n - 1], wt, val, n - 1)

        # 선택한 경우와 선택하지 않은 경우 중 더 큰 가치를 반환한다.
        return max(valWith, valWithout)


# 동적 계획법 방식
def knapSack_dp(W, wt, val, n):
    # A[i][w] : 가방 용량이 w일 때의 최대 가치를 저장하는 2차원 배열
    A = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # 2중 for문으로 각 아이템의 최대 가치를 계산한다.
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] > w:
                # 현재 아이템의 무게가 가방 용량을 초과하는 경우
                # 이전 아이템의 가치를 그대로 사용한다.
                A[i][w] = A[i - 1][w]
            else:

                valWith = val[i - 1] + A[i - 1][w - wt[i - 1]]  # 현재 아이템을 선택하는 경우
                valWithout = A[i - 1][w]  # 선택하지 않는 경우
                A[i][w] = max(valWith, valWithout)  # 둘 중 가치가 더 큰 경우를 선택한다.
    return A[n][W]


n = int(input())  # 물건들의 수
val = list(map(int, input().split()))  # 물건들의 가치를 저장한 리스트
wt = list(map(int, input().split()))  # 물건들의 무게를 저장한 리스트
W = int(input())  # 현재 배낭의 용량

end_time = time.time()  # 프로그램 종료 시간

print("실행시간 : ", end_time - start_time)  # 프로그램 실행시간 출력
print("배낭 채우기(분할 정복 기법) 최대 가치:", knapSack_dc(W, wt, val, n))  # 분할 정복 기법 출력
print("배낭 채우기(동적 계획법) 최대 가치:", knapSack_dp(W, wt, val, n))  # 동적 계획법 출력
