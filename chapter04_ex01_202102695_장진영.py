# 위상정렬 알고리즘 프로그램
# 시간 복잡도 : O(v + e)
# v : 정점의 수
# e : 간선의 수
import time  # 프로그램 실행시간을 알아보기 위한 모듈

start_time = time.time()  # 프로그램 시작 시간


def topological_sort(graph):
    in_degree = {vtx: 0 for vtx in graph}  # 진입 차수 저장하기 위한 딕셔너리

    for vtx in graph:  # 그래프의 정점을 -> 정점 수 만큼 O(v)
        for nbr in graph[vtx]:  # 정점과 연결된 이웃 정점을
            in_degree[nbr] += 1  # 이웃 정점의 차수를 +1 해준다.

    zero_degree = []  # 진입차수가 0인 정점을 저장하는 리스트
    for vtx in graph:  # 그래프의 정점
        if in_degree[vtx] == 0:  # 진입 차수가 0인 경우
            zero_degree.append(vtx)  # 리스트에 저장

    while zero_degree:  # 저장된 리스트가 빌 때 까지
        curt_v = zero_degree.pop()  # 현재 정점
        print(curt_v, end=' ')  # 현재 정점을 출력
        # 진입 차수가 0인 정점을 제거 하지만 모든 간선을 확인 하므로 O(e)

        for nbr in graph[curt_v]:  # 현재 정점은 탐색 했으므로
            in_degree[nbr] -= 1  # 이웃 정점의 진입 차수를 -1 한다.
            if in_degree[nbr] == 0:  # 진입 차수가 0이 되면
                zero_degree.append(nbr)  # 리스트에 저장한다.


mygraph = dict()  # 그래프 저장 딕셔너리
v = int(input())  # 정점의 개수
e = int(input())  # 간선의 개수
for _ in range(e):
    edge = input().split()  # 연결 된 간선 입력

    if edge[0] not in mygraph:  # 그래프에 정점이 없다면
        mygraph[edge[0]] = set()  # 정점을 키로 추가하고 빈 집합으로 초기화
    if edge[1] not in mygraph:  # 그래프에 정점이 없다면
        mygraph[edge[1]] = set()  # 정점을 키로 추가하고 빈 집합으로 초기화

    mygraph[edge[0]].add(edge[1])  # 방향 그래프 이므로 단 방향만 간선 추가


end_time = time.time()  # 프로그램 종료 시간
print("실행시간 : ", end_time - start_time)  # 프로그램 실행시간 출력
print('topological_sort: ')
topological_sort(mygraph)  # 위상정렬 시작
print()
