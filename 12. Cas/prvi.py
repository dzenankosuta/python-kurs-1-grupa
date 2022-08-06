#  Danas radimo funkcije

# Funkcija predstavlja blok koda koji ce se izvrsiti samo u slucaju pozivanja.

# sintaksa:
from re import A


def naziv_funkcije():
    # kod za izvrsavanje
    print("Odstampaj nesto.")

naziv_funkcije()

# 1. varijanta je umesto print(...) koristimo rec return

def druga_funkcija():
    #  kod za izvrsavanje
    a = 5
    return a 

print(druga_funkcija())

# Napraviti funkciju sa nazivom pozdrav, koja vraca recenicu "Zdravo svima." na dva nacina.
# Preko print() i preko return.

def pozdrav():
    print("Zdravo svima.")

pozdrav()

def pozdrav2():
    return "Zdravo svima."
    # Nakon return unutar funkcije nijedna naredba se vise nece izvrsiti!
    # return staviti iskljucivo na kraju!!!

print(pozdrav2())

# Svaka funkcija moze sadrzati parametre (argumente) u sebi koje ce koristiti za izvrsavanje 
#  odredjenog posla.

def vraca_zbir(a,b): # a i b predstavlaju parametre unutar funkcije.
    return a+b

print(vraca_zbir(4,10)) # 4 i 10 predstavlaju argumente.

#  Pozivanjem funkcije moramo staviti onoliko argumenata koliko smo definisali
#  parametara prilikom definisanja funkcije.

def proizvod(x=5,y=10): # moguce su defaultne vrednosti, ali je njih potrebno definisati kao poslednje.
    return x*y

print(proizvod(7,8))

#  Napraviti funkciju koja vraca kolicnik dva broja. U slucaju da je delilac jednak nuli imamo poruku
#  deljenje nije moguce izvrsiti. Takodje neka delilac ima defaultnu vrednost 1.

def kolicnik(a, b=1):
    if b == 0:
        return "Deljenje nije moguce izvrsiti"
    return a/b

print(kolicnik(10,2))
print(kolicnik(10,0))
print(kolicnik(10))
# print(kolicnik()) greska jer funkcija ocekuje bar jednu vresnost: a


prom1 = 17
def vrati_prom():
    prom1 = 14
    print(prom1)

vrati_prom()

print(prom1)

#  Promenljiva definisana unutar function scope (prostora funkcije) je vidljiva samo unutar 
#  te funkcije. Ako je pozovemo van nje, program je nece prepoznati.

def vrati_nesto():
    prom2 = 16
    print(prom2)

print(prom2)

# Domaci zadaci:
#  1. Napraviti funkciju koja vraca povrsinu pravougaonika na osnovu unetih argumenata. 
#    Odnosno povrsinu kvadrata ako su dva data argumenta jednaka.

#  2. Napraviti funkciju koja pretvara broj incha u cm.
#     Pozivanjem funkcije treba uneti broj incha. 
