graph = {'A': ['B', 'C'],
            'B': ['C', 'A'],
            'C': ['D'],
            'D': ['E'],
            'E': ['F'],
            'F': ['B']}

visited = set()
def DFS(G, S):
    visited.add(S)
    for v in G[S]:
        if v not in visited:
            visited.add(v)
            DFS(G, v)

# def DFS_loop(G):
#     visited = set()
DFS(graph, 'C')

print(visited)
