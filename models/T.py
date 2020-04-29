from models.vertex import Vertex


class T:
    def __init__(self, adj_list):
        # yer_mums_dahg is an adjacency list
        self.adj_list = adj_list
        self.vertices = set()
        self.neighbors_and_vertices = set()
        self.edge_set = set()

    # need to pass in vertices so that i can add the neighbor vertex
    def addVertex(self, vertex, g_vertices, source_val, edge_weight):
        self.vertices.add(vertex)
        self.neighbors_and_vertices.add(vertex)
        if source_val != -1:
            self.edge_set.add((source_val, vertex.val, edge_weight))
        for i in range(len(self.adj_list[0])):
            if self.adj_list[vertex.val][i] != 0:
                self.neighbors_and_vertices.add(g_vertices[i])

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
