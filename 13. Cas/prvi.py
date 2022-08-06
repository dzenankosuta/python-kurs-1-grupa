#  Postoji mogucnost dodele vrednosti nekoj promenljivoj na globalnom prostoru iz funkcije.
#  A to je upotreba kljucne reci global


def prom():
    global x 
    x = 14
    print(x)

prom()

print(x)

#  lambda funkcija i njena primena

# 1.primer
z = lambda a : 2 * a 

print(z(4))

# 2.primer
#  Napraviti lambda funkciju koja vraca zbir uneta tri broja:

zbir_tri = lambda a, b, c : a + b + c

print(zbir_tri(10,20,30))

def zbir_trii(a,b,c):
    return a+b+c

print(zbir_trii(5,5,5))

# Da li lambda funkcija dozvoljava defaultne vrednosti?

proizvod_tri = lambda a, b, c=10 : a*b*c 

print(proizvod_tri(4,6))

# 3.primer  
# Napraviti funkciju koja unutar sebe sadrzi anonimnu (lambda) funkciju
# i vraca dvostruku, trostruku... vrednost unetog argumenta.

def my_function(s):
    x = lambda a : a * s
    return x 

doubler = my_function(2)
print(doubler(4))

tripler = my_function(3)
print(tripler(9))

# Zadatak:

# Napraviti funkciju  koja ispisuje vrednosti date liste jednu ispod druge.
lista = ["Davud", "Danilo", "Seid", "Hana", "Emin"]

def vred_liste(neka_lista):
    for i in neka_lista:
        print(i)
    return "To su bili elementi nase liste."

print(vred_liste(lista))

# Domaci:
# 1. Napraviti funkciju  koja ispisuje vrednosti date liste pored indeksa, jedne ispod drugih.

lista1 = [1 , 5 , 4, "Market", "Ulica", "Park"]

# 2. Napraviti funkciju koja vraca zbir svih elemenata date liste.
lista3 = [1,2,3,4,5]
