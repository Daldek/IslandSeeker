# -*- coding: cp1250 -*-
plik = open('H:\! temp\Map_100x100_v40.txt', 'r')
linie = plik.readlines() #zwraca tablice z kolejnymi linijkami.
plik.close()
wysokosci = []
for i in linie: #dla kazdego wiersza
    rozdzielona = i.split()
    nowa = []
    for j in rozdzielona: #dla kazdej liczby
        nowa.append(float(j))
    wysokosci.append(nowa)

h = float(raw_input('Podaj rzedna h wody ')) #pobiera rzedna wysokosci

r = [] #takie wyspy, dla ktorych nie znamy jeszcze sasiadow
wyspy = 0 #licznik wysp

m = len(wysokosci[0]) #m liczba kolumn
n = len(wysokosci) #n liczba wierszy

for y in range(n):
    for x in range(m):
        if wysokosci[y][x] == 'q' or wysokosci[y][x] == 'e':  # q to woda e to teren
            pass #juz odwiedzone
        else:
            if h > wysokosci[y][x]: #znaleziono wode
                wysokosci[y][x] = 'q' #q to woda
            else: #znaleziono teren
                wysokosci[y][x] = 'e' #e to teren
                r.append((y,x)) #takie wyspy, dla ktorych nie znamy jeszcze sasiadow
                wyspy = wyspy +1
                while r != []: # != dopoki pozostaja niezbadane fragmety wyspy
                    t = r[0] #teraz badamy sasiadow "t"
                    r.remove(t)
                    sasiedzi = [(t[0]-1, t[1]), (t[0]+1, t[1]), (t[0], t[1]-1), (t[0], t[1]+1)] #(y,x)
                    for i in sasiedzi: #i[0] to y, i[1] to x
                        ix = i[1]
                        iy = i[0]
                        if iy < 0 or iy >= n or ix < 0 or ix >= m: #wartosci poza tablica (mapa)
                            pass
                        elif wysokosci[iy][ix] == 'q' or wysokosci[iy][ix] == 'e': #juz odwiedzony fragment wyspy
                            pass
                        else:
                            if h > wysokosci[iy][ix]:
                                wysokosci[iy][ix] = 'q'
                            else:
                                wysokosci[iy][ix] = 'e'
                                r.append((iy,ix))


print 'Przy wysokosci ', h, ' jest ', wyspy, ' wysp'
