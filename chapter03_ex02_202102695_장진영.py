# 순서쌍들의 집합에서 가장 가까운 두 점의 거리를 계산하는 프로그램
# 순서쌍들을 입력 받고 그 중 가장 가까운 두 점을 찾는다.
# 시간복잡도 : O(n ** 2)
import time
import math  # 루트 연산을 위한 모듈

start = time.time()


def closest_pair(p):
    n = len(p)  # 입력 받은 순서쌍들의 수
    mindist = float("inf")  # 최단 거리
    for i in range(n - 1):  # 반복문 T(n -1) -> T(n)
        for j in range(i + 1, n):  # 반복문 T(n)
            dist = distance(p[i], p[j])  # 거리 계산하는 함수 호출 반환 값 저장
            if dist < mindist:  # 최단거리와 함수 반환 값 비교해서
                mindist = dist  # 최단거리를 변경해줌

    return mindist  # 최단거리 반환


# 유클리드 거리 계산을 위한 함수 정의
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


p = []  # 순서쌍을 저장하는 리스트
n = int(input())
for _ in range(n):
    # input().split() : 한 줄로 받은 입력을 나누어줌
    # map : 나누어준 값을 int형으로 저장
    a, b = map(int, input().split())
    p.append([a, b])  # 입력 값을 리스트 형태로 p에 append

end = time.time()

print("실행시간 : ", end - start)
print("최근점 거리:", closest_pair(p))
