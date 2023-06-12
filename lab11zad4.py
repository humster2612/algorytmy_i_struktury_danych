class UnionFind:
    def init(self, wierzcholki):
      
        self.rodzic = {}
        self.ranga = {}
        for wierzcholek in wierzcholki:
          
            self.rodzic[wierzcholek] = wierzcholek
            
            self.ranga[wierzcholek] = 0

            
    def znajdz(self, wierzcholek):
        if self.rodzic[wierzcholek] != wierzcholek:
          
            self.rodzic[wierzcholek] = self.znajdz(self.rodzic[wierzcholek])
            
        return self.rodzic[wierzcholek]

    def scal(self, wierzcholek1, wierzcholek2):
      
        korzen1 = self.znajdz(wierzcholek1)
        korzen2 = self.znajdz(wierzcholek2)
        
        if korzen1 != korzen2:
            if self.ranga[korzen1] < self.ranga[korzen2]:
              
                self.rodzic[korzen1] = korzen2
                
            elif self.ranga[korzen1] > self.ranga[korzen2]:
              
                self.rodzic[korzen2] = korzen1
            else:
              
                self.rodzic[korzen2] = korzen1
                
                self.ranga[korzen1] += 1


def kruskal(graph):
  
    minimalne_drzewo_rozpinajace = []
    krawedzie = []
    
    for wierzcholek in graph:
        for sasiad in wierzcholek.getConnections():
          
            waga = wierzcholek.getWeight(sasiad)
            krawedzie.append((wierzcholek.getId(), sasiad.getId(), waga))
            

    krawedzie.sort(key=lambda x: x[2])

    wierzcholki = list(graph.getVertices())
    
    zbior_razy = UnionFind(wierzcholki)
    

    for krawedz in krawedzie:
        wierzcholek1, wierzcholek2, waga = krawedz
        
        if zbior_razy.znajdz(wierzcholek1) != zbior_razy.znajdz(wierzcholek2):
          
            zbior_razy.scal(wierzcholek1, wierzcholek2)
            
            minimalne_drzewo_rozpinajace.append(krawedz)

    return minimalne_drzewo_rozpinajace
