import heapq

def prim(graph):
  
    minimalne_drzewo_rozpinajace = []
    
    startowy_wierzcholek = next(iter(graph))
    
    odwiedzone = set([startowy_wierzcholek])
    
    krawedzie = [(waga, startowy_wierzcholek, sasiad) for sasiad, waga in startowy_wierzcholek.connectedTo.items()]
    
    heapq.heapify(krawedzie)

    while krawedzie:
        waga, obecny_wierzcholek, nastepny_wierzcholek = heapq.heappop(krawedzie)
        
        if nastepny_wierzcholek not in odwiedzone:
          
            odwiedzone.add(nastepny_wierzcholek)
            
            minimalne_drzewo_rozpinajace.append((obecny_wierzcholek.getId(), nastepny_wierzcholek.getId(), waga))
            
            
            for sasiad, waga in nastepny_wierzcholek.connectedTo.items():
              
              
                if sasiad not in odwiedzone:
                  
                  
                  
                    heapq.heappush(krawedzie, (waga, nastepny_wierzcholek, sasiad))

    return minimalne_drzewo_rozpinajace
