#E40 

def LongestPath_DAG(source, sink, edges):
    graph = {}
    for i in edges:
        u, rest = i.split("->")
        v, w= rest.split(":")
        u, v, w = int(u), int(v), int(w)
        
        if u not in graph:
            graph[u] = []

        graph[u].append((v,w))
    
    indegree = {}

    for u in graph:
        if u not in indegree:
            indegree[u] = 0

        for v, w in graph[u]:
            if v not in indegree:
                indegree[v] = 0
            indegree[v] += 1 
    
    queue = []

    for node in indegree:
        if indegree[node] == 0:
            queue.append(node)

    order = []
    while queue:
        u = queue.pop(0)
        order.append(u)

        if u in graph:
            for v, w in graph[u]:
                indegree[v] -=  1
                if indegree[v] == 0:
                    queue.append(v)

    dist = {}

    for node in order:
        dist[node] = float("-inf")

    dist[source] = 0

    prev = {}

    for u in order:
        if u in graph:
            for v,w  in graph[u]:
                if dist[u] + w > dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u
    
    length = dist[sink]

    path = []
    node = sink
    while node in prev:
        path.append(node)
        node = prev[node]
    path.append(source)
    path.reverse()

    return str(length) + "\n" + "->".join(map(str, path))

    



edges = [
    "28->32:23", "11->37:11", "11->30:9", "28->36:29", "8->34:23",
    "2->5:21", "17->27:23", "28->40:17", "2->12:1", "6->18:32",
    "6->11:9", "9->17:2", "16->40:24", "20->31:12", "8->26:18",
    "20->39:29", "12->26:18", "0->22:21", "0->24:33", "13->37:20",
    "11->12:22", "32->34:20", "32->37:16", "27->41:23", "12->31:1",
    "13->25:26", "13->27:6", "22->35:30", "22->32:6", "13->23:17",
    "5->32:23", "22->38:2", "10->28:28", "35->36:1", "10->23:9",
    "24->36:39", "10->26:24", "24->31:19", "22->29:31", "4->16:0",
    "31->34:5", "29->39:24", "16->37:24", "18->37:16", "24->29:9",
    "10->35:7", "3->11:12", "10->33:8", "1->24:11", "1->20:8",
    "5->12:10", "5->14:16", "19->20:21", "26->39:32", "19->36:8",
    "18->42:0", "10->40:1", "4->34:8", "23->27:35", "9->20:0",
    "25->26:32", "4->26:30", "34->38:15", "4->28:23", "0->12:22",
    "0->15:11", "8->17:23", "3->27:27", "1->9:23", "7->27:28",
    "7->28:32", "1->7:18", "1->2:15", "3->42:29", "9->32:1",
    "6->38:0", "14->17:24", "6->31:16", "15->23:15", "15->25:36",
    "15->28:37", "3->32:4", "5->40:31", "16->19:1", "17->33:17",
    "2->26:26", "2->27:7", "13->14:36", "3->39:28", "7->33:29"
]
print(LongestPath_DAG(16, 40, edges))




