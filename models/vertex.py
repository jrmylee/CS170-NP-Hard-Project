class Vertex:
    def __init__(self, val, total_weight, degree):
        self.val = val
        self.total_weight = total_weight
        self.degree = degree
        self.new_degree = degree

        self.connected = []
        self.cum_pairs_cost = 0

    def set_degree(self, new_deg):
        self.degree = new_deg
        self.new_degree = new_deg

    def set_total_weight(self, new_weight):
        self.total_weight = new_weight

    def set_new_degree(self, new_deg):
        self.new_degree = new_deg

    def __lt__(self, other):
        return self.val < other.val
