class Vertex:
    def __init__(self, val, total_weight, degree):
        self.val = val
        self.total_weight = total_weight
        self.degree = degree
    
    def set_degree(self, new_deg):
        self.degree = new_deg

    def set_total_weight(self, new_weight):
        self.total_weight = new_weight