from models.vertex import Vertex


class T:
    def __init__(self, adj_list, dijkstra_container):
        # yer_mums_dahg is an adjacency list
        self.adj_list = adj_list
        self.vertices = set()
        self.neighbors_and_vertices = set()
        self.edge_set = set()
        self.cost = 0
        self.dijkstra_container = dijkstra_container

    # need to pass in vertices so that i can add the neighbor vertex
    def addVertex(self, vertex, g_vertices, source_val, edge_weight):
        self.vertices.add(vertex)
        self.neighbors_and_vertices.add(vertex)
        if source_val != -1:
            self.edge_set.add((source_val, vertex.val, edge_weight))
        for i in range(len(self.adj_list[0])):
            if self.adj_list[vertex.val][i] != 0:
                self.neighbors_and_vertices.add(g_vertices[i])

        #extra stuff for other cost function
        #helper to update all paircosts
        def dfs(v, prev, curr_sum):
            curr_sum += self.adj_list[v.val][prev.val]
            for i in range(len(v.connected)):
                next = v.connected[i]
                if next.val == prev.val:
                    continue
                vertex.cum_pairs_cost += curr_sum
                dfs(next, v, curr_sum)

        if source_val != -1: #anything past the first node in t
            #adds the new cost to T
            size = len(self.vertices)
            edge_weight = self.adj_list[vertex.val][g_vertices[source_val].val]
            added_cost = g_vertices[source_val].cum_pairs_cost + size * edge_weight
            self.cost += added_cost
            #updates all the vertices cost function
            g_vertices[source_val].connected.append(vertex)
            vertex.connected.append(g_vertices[source_val])
            dfs(g_vertices[source_val], vertex, 0)
    
    # does not use T's shortest paths; need to modify
    def averagePairwiseCost(self):
        count = 0
        cost = 0
        for source in self.vertices:
            for dest in self.vertices:
                count += 1
                if source.val == dest.val:
                    continue
                else:
                    cost += self.dijkstra_container[source.val][0][dest.val]
        return cost/count


            



    def isComplete(self, g_vertices):
        for vertex in g_vertices:
            if vertex not in self.neighbors_and_vertices:
                return False
        return True

    def printT(self, filename):
        f = open(filename, 'w')

        for vertex in self.vertices:
            f.write(str(vertex.val) + " ")
        f.write("\n")
        for edge in self.edge_set:
            f.write(str(edge[0]) + " " + str(edge[1]) + "\n")
