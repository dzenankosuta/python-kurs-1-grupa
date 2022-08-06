# Domaci.
# Koristeci bool() funkciju ispitati sledece stvari:
lista1 = [0]
# 1. Da li je string koji je uneo korisnik True ili False
# 2. Da li je broj koji je uneo korisnik True ili False
# 3. Da li je lista1 True ili False
# 4. Uporediti dva uneta broja od strane korisnika.

# 1.
recenica1 = str(input("Unesite neki string: "))
print(bool(recenica1))

# 2.
broj1 = int(input("Unesite neki broj: "))
print(bool(broj1))

# 3.
print(bool(lista1))

# 4.
broj2 = int(input("Unesite prvi broj: "))
broj3 = int(input("Unesite drugi broj: "))

if bool(broj2>broj3):
    print("Prvi uneti broj je veci od drugog")
elif bool(broj2<broj3):
    print("Prvi uneti broj je manji od drugog")
else:
    print("Dva uneta broja su jednaka.")
