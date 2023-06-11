 import heapq
from graphs import *


def zad(graf, start):
  
    odleglosci = {wierzcholek: float('inf') for wierzcholek in graf}
  
  odleglosci[start] = 0
  
  kolejka = []

    heapq.heappush(kolejka, (0, start))

    odwiedzone = set()

  
  while kolejka:
  
  obecna_odleglosc, obecny_wierzcholek = heapq.heappop(kolejka)

        if obecny_wierzcholek in odwiedzone:
            continue

  
  odwiedzone.add(obecny_wierzcholek)

  
  for sasiad, waga in graf[obecny_wierzcholek].items():
  
      odleglosc = obecna_odleglosc + waga

  
  if odleglosc < odleglosci[sasiad]:
  
      odleglosci[sasiad] = odleglosc
                heapq.heappush(kolejka, (odleglosc, sasiad))

    return odleglosci
