# Domaci zadatak:
#  1. Zadatak:
#  Napraviti dva niza od po 6 elemenata. Neka se izvrsi iteracija tako da
#  se element prvog niza prikaze onoliko puta koliko ima elemenata drugog niza
#  a pritom i svaki element drugog niza(ugnjezdena for petlja).

#   2. Zadatak:
#  Ispisati sve parne prirodne brojeve od 10 do 110 (ukljucujuci oba) izuzev 
#  16,22,44,66,88,102,108.

#  3. Zadatak:
#  Ispisati sve elemente prethodno definisane liste od 10 elemenata odpozadi.

niz1 = [1,2,3,4,5,6]
niz2 = ["banana", "jabuka", "kruska", "ananas", "kivi", "jagoda"]

for i in niz1:
    for j in niz2:
        print(i,j)


for i in range(10,111,2):
    if i == 16 or i == 22 or i == 44 or i == 66 or i == 88 or i == 102 or i == 108:
        continue
    print(i)

lista = ["banana", "jabuka", "kruska", "ananas", "kivi", "jagoda", "nar", "mango", "narandza", "mandarina"]

duzina = len(lista)
print(duzina)
for i in range(duzina - 1,-1,-1):
    print(lista[i])
