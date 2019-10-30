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

def BFS_shortest_graph(G, S):
    visited = set()
    visited.add(S)
    Q = Queue()
    Q.put(S)
    dist = {V:0 if V == S else {V:float('inf')} for V in G}

    while not Q.empty():
        v = Q.get()
        for edge in G[v]:
            if edge not in visited:
                dist[edge] = dist[v] + 1
                visited.add(edge)
                Q.put(edge)
    return dist


def connected_components(G):
    visited = set()
    n = len(G)

    for i in G.keys():
        if i not in visited:
            visited.add(BFS(G, i))
    
    return visited


# vis = BFS(graph, 'A')
vis = BFS_shortest_graph(graph, 'A')


print(vis)