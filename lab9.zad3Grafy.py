from graphs import Graph


def zadGraph():
    g = Graph()

    num_werchol = int(input("Podaj ilość wierzchołków: "))
    
    for i in range(num_werchol):
      
        klcz = input("Podaj identyfikatory wierzchołków: ")
        
        g.addVertex(klcz)

    num_krw = int(input("Podaj ilość krawędzi: "))
    for i in range(num_krw):
        from_vertex = input("Podaj wierzchołek początkowy: ")
        
        to_vertex = input("Podaj wierzchołek ostatnij: ")
        
        cost = int(input("Podaj wagę krawędzi: "))
        
        g.addEdge(from_vertex, to_vertex, cost)

    return g


graph = zadGraph()

print("Wierzchołki: ")
for vertex in graph.getVertices():
  
    print(vertex)

print("Krawędzi: ")
for vertex in graph:
  
    for neighbor in vertex.getConnections():
      
      
        print(f"{vertex.getId()} --> {neighbor.getId()} (waga: {vertex.getWeight(neighbor)})")
