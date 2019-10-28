from queue import Queue

graph = {'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'D': ['E'],
            'E': ['F'],
            'F': ['C']}

def BFS(G, S):
    visited = set()
    visited.add(S)
    Q = Queue()
    Q.put(S)

    while not Q.empty():
        v = Q.get()
        for edge in G[v]:
            if edge not in visited:
                visited.add(edge)
                Q.put(edge)
    return visited

vis = BFS(graph, 'A')

print(vis)