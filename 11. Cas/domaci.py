# Domaci:
#  1. Koristiti while petlju gde ce korisnik unositi prirodne brojeve
#     i oni ce se ispisivati sve do momenta kada korisnik unese broj 149.


#  2.  Ispisati sve elemente, kao i indekse (element, indeks na kom se nalazi element)
#      prethodno definisane liste od 10 elemenata odpozadi.


# 1.
broj = int(input("Unesite neki prirodan broj: "))
while broj != 149:
    print(broj)
    broj = int(input("Unesite neki prirodan broj: "))


# 2.
voce = ["banana", "jabuka", "kruska", "ananas", "kivi", "jagoda", "nar", "mango", "narandza", "mandarina"]
duzina = len(voce)

for i in range(duzina - 1, -1,-1):
    print(voce[i],i)