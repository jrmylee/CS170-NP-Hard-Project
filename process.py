from models.T import *
from utils import *

# G is
# T should be a dahg
# take max degree vertex (v), add to t

# go to v, we get vs neighbors
# for each neighbor (n), check n's neighbors.
# Change n's "degree" to the number of neighbors that are not in T.neighbors_and_vertices

# HERE modify the "new degree of all vertices"
# look at all neighbors of current max degree vertex, choose the neighbor that has the highest "new degree"


def get_neighbors(vertex, adj):
    n = []
    for i in range(len(adj)):
        neighbor = adj[vertex.val][i]
        if neighbor != 0:
            n.append(neighbor)
    return n


def computeCost(t, filename):
    t.printT(filename)
    return 1
    # TODO


def process(v, adj, filename):
    # print(adj[1][0])
    t = T(adj)

    def initial_fun(vertex):
        outgoing_weight = 0
        for i in range(len(adj[0])):
            outgoing_weight = max(outgoing_weight, adj[i][vertex.val])
        if outgoing_weight == 0:
            return float('inf')
        return vertex.new_degree / outgoing_weight

    # returns the minimum cost, edge weight, and edge end vertex
    def cost_function(vertex):
        distances = dijkstras(v, adj, vertex)
        min_distance = float('inf')
        destination = None
        for vert in t.vertices:
            if distances[vert.val] < min_distance:
                min_distance = distances[vert.val]
                destination = vert.val
        if min_distance == float('inf'):
            return float('inf')
        if vertex.new_degree == 0:
            return float('inf')
        return (2**(min_distance/vertex.new_degree), min_distance, destination)

    max_deg_vert = v[0]

    for vert in v:
        max_deg_vert = max(vert, max_deg_vert, key=initial_fun)

    for i in range(len(adj)):
        if adj[i][max_deg_vert.val] != 0:
            v[i].new_degree -= 1
    t.addVertex(max_deg_vert, v, -1, -1)

    while not t.isComplete(v):
        # look through all vertices in T, check their neighbors
        max_deg_vert = None
        edge_vert = None
        edge = None

        cur_cost = None 
        min_cost = None

        for vert in v:
            if vert in t.vertices:
                continue
            cur_cost = cost_function(vert)
            if (max_deg_vert is None or cur_cost[0] < min_cost):
                max_deg_vert = vert
                edge_vert = v[cur_cost[2]]
                edge = cur_cost[1]
                min_cost = cur_cost

        for i in range(len(adj)):
            if adj[i][max_deg_vert.val] != 0:
                v[i].new_degree -= 1

        t.addVertex(max_deg_vert, v, edge_vert.val, edge)

    return computeCost(t, filename)
    # for i in range(len(adj)):
    #     neighbor = adj[max_deg_vert.val][i]
    #     if neighbor != 0:
    #         nn = get_neighbors(neighbor, adj)
    #         adj[max_deg_vert.val][i] = 0
    #         for n in nn:
    #             if n not in t.neighbors_and_vertices:
    #                 adj[max_deg_vert.val][i] += 1
