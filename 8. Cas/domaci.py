# Domaci Zadaci:
#  1. Napisati program kojim se unose dva pozitivna cela broja a i b. Napisati program
#     koji izracunava i stampa povrsinu kvadrata ako su uneti brojevi jednaki,
#     odnosno povrsinu pravougaonika ako su brojevi razliciti.
#     Uneti brojevi predstavljaju stranice pravougaonika odnosno kvadrata.


#  2. Proveriti da li uneti broj x pripada intervalu (10,50].
#     Ispisati poruku "Pripada", ili "Ne pripada".

#  3. Korisnik unosi 2 realna broja x i y. Napisati program koji izracunava i stampa,
#     kolicnik (x:y) ako je broj y razlicit od nule, a inace ispisuje poruku deljenje je nemoguce.


# 1. Zadatak:

a = int(input("Unesite prvi pozitivan broj: "))
b = int(input("Unesite drugi pozitivan broj: "))

if a==b:
    print(f"Povrsina kvadrata je {a*b}.")
else:
    print("Povrsina pravougaonika je {}.".format(a*b))


# 2. Zadatak

x = int(input("Unesite neki ceo broj: "))

# 1. Nacin
# if x>10 and x<=50:
#     print("Pripada")
# else:
#     print("Ne pripada")

#  2. Nacin
if x in range(11,51):
    print("Pripada")
else:
    print("Ne pripada")

# 3. Zadatak

x = float(input("Unesite prvi realan broj: "))
y = float(input("Unesite drugi realan broj: "))

if y==0:
    print("Deljenje je nemoguce.")
else:
    print(f"Kolicnik dva uneta realna broja je {x/y}")