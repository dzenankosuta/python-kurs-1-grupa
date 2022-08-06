# Domaci:
# 1. Napraviti funkciju  koja ispisuje vrednosti date liste pored indeksa, jedne ispod drugih.

lista1 = [1 , 5 , 4, "Market", "Ulica", "Park"]

# 2. Napraviti funkciju koja vraca zbir svih elemenata date liste.
lista3 = [1,2,3,4,5]


# 1.
def vrednosti_indeksi(lista):
    duzina = len(lista)
    for i in range(0, duzina):
        print(i, lista[i])

vrednosti_indeksi(lista1)

# 2.
def zbir_elemenata(lista):
    zbir_elemenata = 0
    for i in lista:
        zbir_elemenata += i
    return zbir_elemenata

print(zbir_elemenata(lista3))