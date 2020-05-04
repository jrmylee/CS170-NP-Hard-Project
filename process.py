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
    # there is an array that contains index for source vertex, and then contains distances array and prev array
    dijkstra_container = []
    for vert in v:
        distances, prev = dijkstras(v, adj, vert)
        dijkstra_container.append([distances, prev])
    t = T(adj, dijkstra_container, v)

    def initial_fun(vertex):
        outgoing_weight = float('inf')
        for i in range(len(adj[0])):
            if adj[i][vertex.val] < outgoing_weight and i != vertex.val:
                outgoing_weight = adj[i][vertex.val]
        if outgoing_weight == 0 or vertex.new_degree == 0:
            return float('inf')
        return outgoing_weight / vertex.new_degree

    # returns the minimum cost, edge weight, and edge end vertex
    def cost_function(vertex, dijkstra_container):
        distances, prev = dijkstra_container[vertex.val][0], dijkstra_container[vertex.val][1]
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
        prev_arr.append(temp)
        return (((min_distance))/vertex.new_degree, min_distance, destination, prev_arr)

    min_cost_vertex = v[0]

    for vert in v:
        min_cost_vertex = min(vert, min_cost_vertex, key=initial_fun)

    for i in range(len(adj)):
        if adj[i][min_cost_vertex.val] != 0:
            v[i].new_degree -= 1
    t.addVertex(min_cost_vertex, v, -1, -1)

    while not t.isComplete(v):
        # look through all vertices in T, check their neighbors
        min_cost_vertex = None
        edge = None
        prev = []

        cur_cost = (float('inf'), float('inf'), None, [])
        min_cost = (float('inf'), float('inf'), None, [])
        for vert in v:
            if vert in t.vertices:
                continue
            cur_cost = cost_function(vert, dijkstra_container)
            if (min_cost_vertex is None or cur_cost[0] < min_cost[0]):
                min_cost_vertex = vert
                edge = cur_cost[1]
                min_cost = cur_cost
                prev = cur_cost[3]
        if edge == float('inf'):
            t.addVertex(min_cost_vertex, v, -1, -1)
        else:
            # for loop between all edges from cost function prev array
            for i in range(1, len(prev)):
                t.addVertex(v[prev[i]], v, prev[i-1], adj[prev[i-1]][prev[i]])
                for j in range(len(adj)):
                    if adj[j][prev[i]] != 0:
                        v[j].new_degree -= 1  
    for i in v:
        for j in v:
            if adj[i.val][j.val] == 0:
                continue
            old_t_cost = t.cost
            old_t_vertices = t.vertices
            old_t_edgeset = t.edge_set
            old_t_neighborsandvertices = t.neighbors_and_vertices
            if (i.val, j.val, adj[i.val][j.val]) in t.edge_set or (j.val, i.val, adj[i.val][j.val]) in t.edge_set:
                continue
            else:
                if i in t.vertices:
                    if adj[i.val][j.val] < old_t_cost:
                        if j not in t.vertices:
                            t.addVertex(j, v, i.val, adj[i.val][j.val])
                            new_t_cost = t.cost
                            if old_t_cost < new_t_cost:
                                t.redo(adj, dijkstra_container, v, old_t_vertices, old_t_neighborsandvertices, old_t_edgeset, old_t_cost)
    mst_vertices = []
    mst_vertex_dict = {}
    reverse_dict = {}
    edge_weights = [[0 for i in range(len(t.vertices))] for j in range(len(t.vertices))]
    count = 0
    for vertex in t.vertices:
        mst_vertex_dict[count] = vertex.val
        reverse_dict[vertex.val] = count
        temp = Vertex(count, 0, 0)
        mst_vertices.append(temp)
        count+=1
    count = 0
    for vertex in t.vertices:
        for v2 in t.vertices:
            if dijkstra_container[vertex.val][0][v2.val] == 0:
                continue
            edge_weights[count][reverse_dict[v2.val]] = dijkstra_container[vertex.val][0][v2.val]
        count += 1
    g = MST(mst_vertices, edge_weights)
    tempT = T(adj, dijkstra_container, v)
    for edge in g:
        tempT.addEdge(v[mst_vertex_dict[edge[0]]], v[mst_vertex_dict[edge[1]]], edge[2])
    old = t.cost
    if tempT.cost < t.cost:
        t = tempT
    if old < t.cost:
        print("YUH")
        exit()
    return computeCost(t, filename)