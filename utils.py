from heapq import *

# takes in vertices list with vertex nodes, adjacency list for the graph, and the source vertex


class special_tup:
    def __init__(self, tup):
        self.tup = tup

    def get_priority(self):
        return self.tup[0]

    def get_v(self):
        return self.tup[1]

    def __lt__(self, other):
        return self.tup[0] < other.tup[0]

def dijkstras(vertices, l, s):
    distances = [float('inf')] * len(vertices)
    distances[s.val] = 0
    Q = [special_tup((0, vertices[s.val]))]
    prev = [-1] * len(vertices)
    seen = set()
    while Q:
        U = heappop(Q)
        u = U.get_v().val
        if u not in seen:
            seen.add(u)
            for i in range(len(l[0])):
                if l[u][i] == 0:
                    continue
                if l[u][i] in seen: 
                    continue
                if distances[i] > distances[u] + l[u][i]:
                    distances[i] = distances[u] + l[u][i]
                    prev[i] = u
                    heappush(Q, special_tup((distances[i], vertices[i])))
    return distances, prev