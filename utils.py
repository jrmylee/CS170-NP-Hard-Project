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


def dijkstras(vertices, l, s, flag=False):
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
                if distances[i] > distances[u] + l[u][i]:
                    distances[i] = distances[u] + l[u][i]
                    prev[i] = u
                    heappush(Q, special_tup((distances[i], vertices[i])))
    # if flag == True:
    #     print(s.val)
    #     print(distances)
    #     exit()
    return distances, prev


def averagePairwiseCost(t, vertices, adj=None, dijkstra_container=None):
    count = 0
    cost = 0
    if dijkstra_container == None:
        dijkstra_container = [0 for j in range(len(vertices))]
        for vert in vertices:
            if vert in t.vertices:
                if vert.val != 24:
                    distances, prev = dijkstras(vertices, adj, vert, True)
                else:
                    distances, prev = dijkstras(vertices, adj, vert)
            else:
                distances, prev = [], []
            dijkstra_container[vert.val] = [distances, prev]
    for source in t.vertices:
        for dest in t.vertices:
            count += 1
            if source.val == dest.val:
                continue
            else:
                cost += dijkstra_container[source.val][0][dest.val]
    return cost/count


def MST(vertices, l):
        reached_set = set()
        reached_set.add(vertices[0])
        unreached_set = set()
        num_edges = 0
        edge_set = set()
        for i in range(1, len(vertices)):
            unreached_set.add(vertices[i])
        while num_edges < len(vertices)-1:
            min = float('inf')
            v1 = None
            v2 = None
            for vertex in reached_set:
                for dest in unreached_set:
                    if l[vertex.val][dest.val] != 0 and min > l[vertex.val][dest.val]:
                        v1 = vertex
                        v2 = dest
                        min = l[vertex.val][dest.val]
            edge_set.add((v1.val, v2.val, min))
            unreached_set.remove(v2)
            reached_set.add(v2)
            num_edges += 1
        return edge_set
                    
            