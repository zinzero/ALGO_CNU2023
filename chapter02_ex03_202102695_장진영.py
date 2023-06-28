# 실행시간을 계산하기 위해 time 모듈을 import함
import time

# 프로그램 실행 시작 시간
start = time.time()


def binary_digits(n):
    # 입력값이 1 이하 : 자릿수는 1이므로 1을 반환
    if n <= 1:
        return 1
    # T([n /2]) + 1
    else:
        # 입력값을 2로 나누어 자릿수를 계산
        # 재귀 호출은 입력값을 2로 나눈 횟수에 비례하게 이루어짐 n = 2^k
        return 1 + binary_digits(n // 2)

# 프로그램 실행 종료 시간
end = time.time()

n = int(input())

# 실행시간 계산
print("실행시간 = ", end - start)
print(binary_digits(n))
# 시간복잡도 : O(log2 n)
