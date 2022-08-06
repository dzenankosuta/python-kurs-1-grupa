# Domaci zadatak. Traziti od korisnika unos 4 broja.
# Zatim izvrsiti poredjenje zbira prva dva broja sa zbirom druga dva broja.
# Nakon poredjenja zbira izvrsiti poredjenje razlike.


a = int(input("Unesite prvi broj: "))
b = int(input("Unesite drugi broj: "))
c = int(input("Unesite treci broj: "))
d = int(input("Unesite cetvrti broj: "))

if a + b > c + d:
    print("Zbir prva dva uneta broja je veci od zbira druga dva uneta broja.")
elif a + b < c + d:
    print("Zbir prva dva uneta broja je manji od zbira druga dva uneta broja.")
else:
    print("Zbir prva dva uneta broja je jednak zbiru druga dva uneta broja.")


if a - b > c - d:
    print("Razlika prva dva uneta broja je veca od razlike druga dva uneta broja.")
elif a - b < c - d:
    print("Razlika prva dva uneta broja je manja od razlike druga dva uneta broja.")
else:
    print("Razlika prva dva uneta broja je jednaka razlici druga dva uneta broja.")
