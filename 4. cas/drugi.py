# Menjanje tipa podatka

x = 4

print(type(x))

#  Konverzacija iz tipa int u tip float
y = float(x)

print(y)

z = str(x)

print(type(z))

#  Nece se izvrsiti sledece sabiranje jer je z="4", a spajanje stringa i brojeva nije moguce.
# print(2 + z)

w = int(z)

#  Moguca je konverzacija stringa "4" u tip int
print(w)
print(type(w))

#  Moguca je konverzacija stringa "4" u tip float
q = float(z)
print(q)
print(type(q))

#  sledeca konverzija nece biti moguca
# novi_string = "4 banane kostaju 96 dinara."
# novi_int = int(novi_string)
# print(novi_int)

# jos jedan primer gde nije moguce izvrsiti konverziju
# novi_string = "50 40"
# novi_int = int(novi_string)
# print(novi_int)

# Zakljucak je da konverziju stringa u int ili float je moguce izvrsiti samo u slucaju
#  da se unutar stringa nalazi samo jedan broj, svi ostali slucajevi nam daju error.