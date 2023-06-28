# 무방향 그래프의 넓이 우선 탐색 프로그램
# 시간복잡도
# 인접 리스트 : O(n + e)
# 인접 행렬 : O(n^2)
# n : 정점의 수
# e : 간선의 수
import time  # 프로그램 실행시간을 알아보기 위한 모듈
import queue  # 큐를 활용하기 위한 모듈

start_time = time.time()  # 프로그램 시작 시간

visited = set()  # 방문 노드 집합


def bfs(graph, start):
    visited.add(start)  # 방문 노드 추가
    que = queue.Queue()  # 큐 생성
    que.put(start)  # 현재 노드를 큐에 저장

    while not que.empty():  # 큐가 비어있지 않을 때까지 반복
        v = que.get()  # 큐에서 맨 처음 노드를 가져오기
        print(v, end=" ")
        nbr = graph[v] - visited  # 그래프의 연결된 점들과 방문한 점을 뺀 나머지 이웃한 점들을 구한다.
        for u in nbr:  # 해당 노드들에 대해서
            visited.add(u)  # 방문한 노드로 넣고
            que.put(u)  # 큐에 추가

            # 정점의 개수 n과 비례하여 O(n)
            # 간선의 개수 e와 비례하므로 O(e)
            # 각각 한 번 씩 처리 되므로 O(n +e)


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
print('BFS : ', end='')
bfs(mygraph, "A")  # BFS 탐색 시작
print()
