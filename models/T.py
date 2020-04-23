import Vertex
class T:
    def __init__(self, adj_list):
        # yer_mums_dahg is an adjacency list
        self.adj_list = adj_list
        self.vertices = set()
        self.neighbors_and_vertices = set()

    #need to pass in vertices so that i can add the neighbor vertex
    def addVertex(self, vertex, g_vertices):
        self.vertices.add(vertex)
        self.neighbors_and_vertices.add(vertex)
        for i in len(self.adj_list[0]):
            if self.adj_list[vertex.val][i] != 0:
                self.neighbors_and_vertices.add(g_vertices[i])

    def isComplete(self, g_vertices):
        for vertex in g_vertices:
            if vertex not in self.vertices:
                return False
        return True