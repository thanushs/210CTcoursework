edgeList = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ']
class Vertex:
    def init(self, n):
        self.name = n
        self.neighbours = list()
    def addNeighbour(self, v):
        if v not in self.neighbours:
            self.neighbours.append(v)
            self.neighbours.sort()

class Graph:
    vertices = {}

    def addVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def addEdge(self, u, v):
        if u in self.vertices and v in self.verties:
            for key, value in self.vertices.items():
                if key == u:
                    value.addNeighbour(v)
                if key == v:
                    value.addNeighbour(u)
            return True
        else:
            return False

    def printGraph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbours))
g = Graph()
a = Vertex()
g.addVertex('A')
for i in range(ord('A'), ord('G')):
    g.addVertex(Vertex(chr(i)))
for edge in edgeLists:
    g.addEdge(edgeList[:1], edgeList[1:])

g.printGraph()

    
