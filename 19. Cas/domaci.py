# Domaci:
# napraviti jos jednu listu koju cine elementi poslednje izmenjene liste, ali da svi budu ispisani
# velikim slovom.

lista = ["ananas", "banana", "kruska", "dinja", "jabuka", "kajsija"]

lista2 = [i.upper() for i in lista]
lista3 = [i.capitalize() for i in lista]
print(lista2)
print(lista3)