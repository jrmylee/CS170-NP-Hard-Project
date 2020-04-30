import heapq

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


def dijkstras(vertices, adj_list, u):
    distances = [float('inf')] * len(vertices)
    distances[u.val] = 0
    Q = []
    for i in range(len(vertices)):
        if vertices[i] == u:
            heapq.heappush(Q, special_tup((0, vertices[i])))
        else:
            heapq.heappush(Q, special_tup((float('inf'), vertices[i])))
    while Q != []:
        min_distance_vertex = heapq.heappop(Q)
        for j in range(len(adj_list[0])):
            if adj_list[min_distance_vertex.get_v().val][j] == 0:
                continue
            alternate_distance = distances[min_distance_vertex.get_v().val] + \
                adj_list[min_distance_vertex.get_v().val][j]
            if alternate_distance < distances[j]:
                distances[j] = alternate_distance
    return distances
