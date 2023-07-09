import queue

mygraph = {"A": {"B", "C"},
           "B": {"A", "D"},
           "C": {"A", "D", "E"},
           "D": {"B", "C", "F"},
           "E": {"C", "G", "H"},
           "F": {"D"},
           "G": {"E", "H"},
           "H": {"E", "G"}
           }

visited = set()


def dfs(graph, start, visited):
    if start not in visited:
        visited.add(start)
        print(start, end=" ")
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)


def bfs(graph, start):
    visited.add(start)
    que = queue.Queue()
    que.put(start)

    while not que.empty():
        v = que.get()
        print(v, end=" ")
        nbr = graph[v] - visited
        for u in nbr:
            visited.add(u)
            que.put(u)


print('DFS : ', end='')
dfs(mygraph, "A", set())
print()
print('BFS : ', end='')
bfs(mygraph, "A")
print()
