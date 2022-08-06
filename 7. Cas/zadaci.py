# 1. Napisati program koji proverava uneti ceo broj x paran ili neparan
#  i ispisuje odgovarajucu poruku.

x = int(input("Unesite neki broj: "))

if x % 2 == 0:
    print("Uneti broj je paran.")
else:
    print("Uneti broj je neparan.")


#  2. Napisati program koji, ako je uneti broj veci od nule, stampa poruku broj je pozitivan.
#  Obuhvatiti i slucajeve kad je broj manji od nule i jednak nuli.

x = int(input("Unesite neki broj: "))

if x < 0:
    print("Uneti broj je negativan.")
elif x > 0:
    print("Uneti broj je pozitivan.")
else:
    print("Uneli ste nulu.")


# 3. Napisati program koji, proverava da li je zbir dva uneta broja deljiv sa 3 ili nije.
#  Ispisati poruku "Jeste" ili "Nije".

x = int(input("Unesite prvi broj: "))
y = int(input("Unesite drugi broj: "))

if (x + y) % 3 == 0:
    print("Jeste.")
else:
    print("Nije.")

# Domaci Zadaci:
#  1. Napisati program kojim se unose dva pozitivna cela broja a i b. Napisati program
#     koji izracunava i stampa povrsinu kvadrata ako su uneti brojevi jednaki,
#     odnosno povrsinu pravougaonika ako su brojevi razliciti.
#     Uneti brojevi predstavljaju stranice pravougaonika odnosno kvadrata.


#  1. Proveriti da li uneti broj x pripada intervalu (10,50].
#     Ispisati poruku "Pripada", ili "Ne pripada".

#  3. Korisnik unosi 2 realna broja x i y. Napisati program koji izracunava i stampa,
#     kolicnik (x:y) ako je broj y razlicit od nule, a inace ispisuje poruku deljenje je nemoguce.
