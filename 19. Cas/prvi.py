lista = ["ananas", "banana", "kruska", "dinja", "jabuka", "kajsija"]
# kroz iteraciju date liste ispisati "BANANA" za svaki element osim gde se nadje "dinja"

lista2 = [i if i=="dinja" else "BANANA" for i in lista]
print(lista2)

# Sortiranje liste. sort() metoda

# 1. Sortiranje prema slovima:

lista = ["kajsija", "jabuka", "ananas", "banana", "kruska", "dinja"]
lista.sort()
print(lista)

# Obrnuti alphabet
lista.sort(reverse=True)
print(lista)

# 2. Sortiranje prema brojevima:
lista2 = [54, 78, -24, 65, -91, 0]

lista2.sort()
print(lista2)

lista2.sort(reverse=True)
print(lista2)

# Po defaultu sort() metoda je (case sensitive)
# Prednost imaju velika slova u odnosu na mala
lista = ["Kajsija", "jabuka", "Ananas", "banana", "Kruska", "dinja"]

lista.sort()
print(lista)
#  U slucaju da zelimo ukinuti prednost velikih slova u odnosu na mala,
#  to mozemo uciniti na sledeci nacin:

lista = ["Kajsija", "jabuka", "Ananas", "banana", "Kruska", "dinja"]

lista.sort(key=str.lower)
print(lista)

# reverse() metoda sluzi za vracanje liste obrnutim redosledom 
# u zavisnosti od redosleda pisanja elemenata u listi.
# 1. primer
lista = ["kajsija", "jabuka", "ananas", "banana", "kruska", "dinja"]
lista.reverse()
print(lista)

# 2. primer
lista2 = [54, 78, -24, 65, -91, 0]
lista2.reverse()
print(lista2)
