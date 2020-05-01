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
    t = T(adj)

    def initial_fun(vertex):
        outgoing_weight = 0
        for i in range(len(adj[0])):
            outgoing_weight = max(outgoing_weight, adj[i][vertex.val])
        if outgoing_weight == 0:
            return float('inf')
        return outgoing_weight / vertex.new_degree

    #returns the new cost of T if new_vertex is added to T through v_in_T, assuming T is connected and a tree
    def cost_function2(vertex, v_in_T, T):
        size = len(T.vertices)
        edge_weight = adj[vertex.val][v_in_T.val]
        added_cost = v_in_T.cum_pairs_cost + size * edge_weight
        return added_cost
        pass



    # returns the minimum cost, edge weight, and edge end vertex
    def cost_function(vertex):
        distances, prev = dijkstras(v, adj, vertex)
        min_distance = float('inf')
        destination = None
        for vert in t.vertices:
            if distances[vert.val] < min_distance:
                min_distance = distances[vert.val]
                destination = vert.val

        # Edge case: disjoint forest
        if min_distance == float('inf'):
            return (float('inf'), float('inf'), -1, [])

        #Edge case: vertex does not connect to anything new
        if vertex.new_degree == 0:
            return (float('inf'), float('inf'), -1, [])

        #TODO come back here

        temp = destination
        prev_arr = []

        #reverse path order
        while temp != vertex.val:
            prev_arr.append(temp)
            temp = prev[temp]
        return (((min_distance)**2)/vertex.new_degree, min_distance, destination, prev_arr)

    min_cost_vertex = v[0]

    for vert in v:
        min_cost_vertex = max(vert, min_cost_vertex, key=initial_fun)

    for i in range(len(adj)):
        if adj[i][min_cost_vertex.val] != 0:
            v[i].new_degree -= 1
    t.addVertex(min_cost_vertex, v, -1, -1)

    while not t.isComplete(v):
        # look through all vertices in T, check their neighbors
        print("t is not complete")
        min_cost_vertex = None
        edge = None
        prev = []

        cur_cost = (float('inf'), float('inf'), None, [])
        min_cost = (float('inf'), float('inf'), None, [])

        for vert in v:
            if vert in t.vertices:
                continue
            cur_cost = cost_function(vert)
            if (min_cost_vertex is None or cur_cost[0] < min_cost[0]):
                min_cost_vertex = vert
                edge = cur_cost[1]
                min_cost = cur_cost
                prev = cur_cost[3]

        for i in range(len(adj)):
            if adj[i][min_cost_vertex.val] != 0:
                v[i].new_degree -= 1
        if edge == float('inf'):
            print('edge == float("inf")')
            t.addVertex(min_cost_vertex, v, -1, -1)
        else:
            # for loop between all edges from cost function prev array
            for i in range(1, len(prev)):
                t.addVertex(v[prev[i]], v, prev[i-1], adj[prev[i-1]][prev[i]])
                for j in range(len(adj)):
                    if adj[j][prev[i]] != 0:
                        v[j].new_degree -= 1  
        

        
    return computeCost(t, filename)
