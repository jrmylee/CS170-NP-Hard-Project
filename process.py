from models.T import T

# G is 
# T should be a dahg
# take max degree vertex (v), add to t

# go to v, we get vs neighbors
# for each neighbor (n), check n's neighbors. 
# Change n's "degree" to the number of neighbors that are not in T.neighbors_and_vertices



#HERE modify the "new degree of all vertices"
# look at all neighbors of current max degree vertex, choose the neighbor that has the highest "new degree"

def get_neighbors(vertex, adj):
    n = []
    for i in range(len(adj)):
        neighbor = adj[vertex.val][i]
        if neighbor != 0:
            n.append(neighbor)
    return n

def process(v, adj):
    t = T(adj)
    new_deg_fun = lambda k: k.new_degree

    while(not t.isComplete(v)):
        max_deg_vert = v[0]
    
        for vert in v:
            max_deg_vert = max(vert, max_deg_vert, key = new_deg_fun)
        
        t.addVertex(max_deg_vert)
        for i in range(len(adj)):
            neighbor = adj[max_deg_vert.val][i]
            if neighbor != 0:
                nn = get_neighbors(neighbor, adj)
                adj[max_deg_vert.val][i] = 0
                for n in nn:
                    if n not in t.neighbors_and_vertices:
                        adj[max_deg_vert.val][i] += 1
                

