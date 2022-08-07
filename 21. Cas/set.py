# Set (Skup) je kolekcija koja je neuredjena (unordered) i neindeksirana (unindexed).
# Setovi se zapisuju u viticastim zagradama.

# Elementi seta su neuredjeni, nepromenljivi i ne dozvoljavaju duplikate.

myset = {"srpski jezik", "matematika", "engleski jezik", "programiranje"}
print(myset)

myset = {"srpski jezik", "matematika", "engleski jezik", "programiranje", "matematika"}
print(myset)

duzina = len(myset)
print(duzina)

tip = type(myset)
print(tip)

# Set moze sadrzati razlicite tipove podataka.
myset2 = {"Vahid", 17, False}
print(myset2)

# for petlja je dozvoljena takodje
for i in myset2:
    if type(i) == int:
        print(i)

# Dodavanje elemenata setu:
# Koristi se set() metoda
myset = {"srpski jezik", "matematika", "engleski jezik", "programiranje"}

myset.add("biologija")

print(myset)

# Sto se tice dodavanja seta drugom setu, to se vrsi pomocu metode update()

myset = {"srpski jezik", "matematika", "engleski jezik"}
myset2 = {"programiranje", "biologija", "fizicko", "hemija"}

myset.update(myset2)
print(myset)

# Za brisanje elemenata se koristi remove() metoda ili discard().
# Postoji jedna razlika izmedju ovde dve metode:
# to je da ako pokusamo da izbrisemo nepostojeci element nekog seta preko remove metode dobicemo error,
#  dok preko discard metode necemo dobiti error.

myset = {"srpski jezik", "matematika", "engleski jezik"}
myset.remove("srpski jezik")
print(myset)

# myset.remove("programiranje")
# print(myset)

myset.discard("engleski jezik")
print(myset)

myset.discard("biologija")
print(myset)

# clear() metoda ce isprazniti ceo set:
myset.clear()
print(myset)

# Preko del mozemo izbrisati ceo set:

# del myset
print(myset)

# Alternativa za update moze biti union() metoda

myset = {"srpski jezik", "matematika", "engleski jezik"}
myset2 = {"programiranje", "biologija", "fizicko", "hemija"}

myset3 = myset.union(myset2)
print(myset3)


myset = {"srpski jezik", "matematika", "programiranje", "biologija"}
myset2 = {"programiranje", "biologija", "fizicko", "hemija"}

# Metoda intersection_update ce nam ostaviti samo one elemente koji su sadrzani u oba seta.
myset.intersection_update(myset2)
print(myset)