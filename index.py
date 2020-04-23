from models.vertex import Vertex

# number, 
# vertex a, vertex b, weight

#parse function
def parse(filename):
    file = open(filename, 'r')
    contents_string = file.read() #reads in as a string
    contents = contents_string.split()
    # print(len(contents))
    contents = [float(elem) for elem in contents]

    n = contents[0]
    adj_list = [[0 for i in range(int(n))] for i in range(int(n))]
    i = 1
    vertices = [None for i in range(int(n))]
    while i < len(contents):
        v1 = int(contents[i])
        v2 = int(contents[i+1])
        adj_list[v1][v2] = contents[i + 2]
        adj_list[v2][v1] = contents[i + 2]
        if vertices[v1] == None:
            vertex = Vertex(v1, contents[i+2], 1)
            vertices[v1] = vertex
        else:
            vertices[v1].set_degree(vertices[v1].degree+1)
            vertices[v1].set_total_weight(vertices[v1].total_weight + contents[i+2])
        if vertices[v2] == None:
            vertex = Vertex(v2, contents[i+2], 1)
            vertices[v2] = vertex
        else:
            vertices[v2].set_degree(vertices[v2].degree+1)
            vertices[v2].set_total_weight(vertices[v2].total_weight+contents[i+2])
        i+=3
    return adj_list, vertices

def main():
    adj_list, vertices_list = parse('./inputs/100.in')
    for elem in vertices_list:
        print(elem.total_weight)
main()

print('dahg')
print("chiesa the genius")
print('degenerate tic tac toe')
print('vodka')