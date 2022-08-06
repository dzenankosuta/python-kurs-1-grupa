
print("Danas je suncan dan.")
print("Danas je suncan dan.")
print("Danas je suncan dan.")
print("Danas je suncan dan.")
print("Danas je suncan dan.")
print("Danas je suncan dan.")
print("Danas je suncan dan.")
print("Danas je suncan dan.")
print("Danas je suncan dan.")
print("Danas je suncan dan.")

# Petlja(ponavljanje) u programiranju predstavlja nacin da se neki kod na laksi nacin
#  izvrsi odredjen broj puta.
#  U Pythonu postoje:
#  1. for   petlja;
#  2. while petlja;

# 1. for petlja:

# 1.primer
for i in range(0,5): # 0 se ukljucuje, 5 se ne ukljucuje
    print(i)

# 2.primer
for i in range(1,11):
    print("Danas je suncan dan.")

# 3.primer
for item in range(7): # ako range poseduje samo jedan argument, taj argument predstavlja krajnji.
    print(item)

# 4.primer
for i in range(1,10,2): # treci argument oznacava korak povecavanja nakon svake iteracije.
    print(i)

# 1. Zadatak
# Napisati sve prirodne brojeve od 4 do 40, sa korakom 3.

for i in range(4,40,3):
    print(i)

# Domaci zadatak.
# 1. Zadatak:
#  Napisati sve parne brojeve od 1 do 50(ukljucujuci 50).

# 2. Zadatak:
#  Napisati sve neparne brojeve od 1 do 100(ukljucujuci 100).

# 3. Napisati sve one brojeve koji su deljivi sa 3 iz intervala (1,201).
