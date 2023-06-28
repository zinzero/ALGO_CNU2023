# 실행시간을 계산하기 위해 time 모듈을 import함
import time

n = int(input())
# 프로그램 실행 시작 시간
start = time.time()


# T(n) = T(n - 1) + 1 + T(n - 1)
def hanoi_tower(n, fr, tmp, to):
    # n이 1인 경우 T(1)
    if n == 1:
        print("원판 1: %s --> %s" % (fr, to))
    # n이 1이 아닌 경우 재귀적으로 호출
    else:
        # 원판 수를 -1 하고 이동 하는 기둥을 변경함 (A, B, C) -> (A, C, B)
        # T(n - 1)
        hanoi_tower(n - 1, fr, to, tmp)
        # T(1)
        print("원판 %d: %s --> %s" % (n, fr, to))
        # 원판 수를 -1 하고 이동 하는 기둥을 변경함 (A, B, C) -> (B, A, C)
        # T(n - 1)
        hanoi_tower(n - 1, tmp, fr, to)

# 프로그램 실행 종료 시간
end = time.time()

# 실행시간 계산
print("실행시간 = ", end - start)
print(hanoi_tower(n, 'A', 'B', 'C'))
# 시간 복잡도 O(2 ** n)
