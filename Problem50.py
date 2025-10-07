#E50
from collections import deque

def TopologicalOrdering(graph):

    order = []

    indegree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1


    candidates = deque([u for u in graph if indegree[u] == 0])

    while candidates:
        u = candidates.popleft()   
        order.append(u)            
        for v in graph[u]:        
            indegree[v] -= 1
            if indegree[v] == 0:
                candidates.append(v)


    if len(order) != len(graph):
        raise ValueError("Input not DAG")

    return order

graph = {
    0:  [12, 18, 19, 2, 25],
    1:  [7],
    10: [23],
    11: [14, 18, 26],
    13: [20, 26],
    14: [24, 28, 29, 30],
    15: [23, 24],
    17: [18, 22],
    18: [22],
    2:  [11, 22, 24, 3],
    20: [23],
    21: [29],
    22: [28],
    23: [30],
    24: [30],
    25: [27, 28],
    28: [29],
    3:  [17, 21, 28, 8],
    4:  [15, 17, 18, 26, 8],
    5:  [14, 18, 19, 28],
    6:  [25, 9],
    7:  [8],
    8:  [15, 17, 24, 25],
    9:  [16, 23, 27, 28],
    12: [],
    16: [],
    19: [],
    26: [],
    27: [],
    29: [],
    30: []
}



Result = TopologicalOrdering(graph)


print(", ".join(map(str, Result)))
