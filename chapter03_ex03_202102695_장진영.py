# 무방향 그래프의 깊이 우선 탐색 프로그램
# 시간복잡도
# 인접 리스트 : O(n + e)
# 인접 행렬 : O(n^2)
# n : 정점의 수
# e : 간선의 수
import time  # 프로그램 실행시간을 알아보기 위한 모듈

start_time = time.time()  # 프로그램 시작 시간


def dfs(graph, start, visited):
    if start not in visited:  # 시작하는 점이 방문한 적 있나 확인
        visited.add(start)  # 없다면 추가하기
        print(start, end=" ")  # 현재 노드 출력
        nbr = graph[start] - visited  # 그래프의 연결된 점들과 방문한 점을 뺀 나머지 이웃한 점들을 구한다.
        for v in nbr:  # 해당 점들에 대해서
            dfs(graph, v, visited)  # 재귀적으로 함수를 호출하여 탐색
            # 정점의 수 많큼 호출 됨 O(n)
            # 간선의 수 만큼 반복함 O(e)
            # 각각 한 번 씩 처리 되므로 O(n + e)


mygraph = dict()  # 그래프 저장 딕셔너리

n = int(input())  # 노드 개수 입력
for _ in range(n):
    edge = input().split()  # 노드 입력

    if edge[0] not in mygraph:  # 딕셔너리에 해당 노드가 없다면
        mygraph[edge[0]] = set()  # 노드를 키로 추가하고 빈 집합으로 초기화
    if edge[1] not in mygraph:  # 딕셔너리에 해당 노드가 없다면
        mygraph[edge[1]] = set()  # 노드를 키로 추가하고 빈 집합으로 초기화

    mygraph[edge[0]].add(edge[1])  # 무방향 그래프 이므로
    mygraph[edge[1]].add(edge[0])  # 양방향으로 간선 추가


end_time = time.time()  # 프로그램 종료 시간
print("실행시간 : ", end_time - start_time)  # 프로그램 실행시간 출력
print('DFS : ', end='')
dfs(mygraph, "A", set())  # DFS 탐색 시작
print()
