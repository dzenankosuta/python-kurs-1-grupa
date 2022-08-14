# Kopija recnika
student = {
    "ime":"Dzenan",
    "prezime":"Kosuta",
    "godina_rodjenja":1996,
    "broj_indeksa":119141,
    "naziv_fakulteta":"DUNP"
}
# Nije dobra praksa. Jer student2 je samo referenca na recnik student.
student2 = student
print(student2)

student2["broj_indeksa"] = 256325
print(student2)
print(student)

# Postoje 2 nacina za kopiju recnika:
# 1.nacin
student = {
    "ime":"Dzenan",
    "prezime":"Kosuta",
    "godina_rodjenja":1996,
    "broj_indeksa":119141,
    "naziv_fakulteta":"DUNP"
}
student2 = student.copy()
print(student2)
student2["broj_indeksa"] = 256325
print(student2)
print(student)

# 2.nacin
student = {
    "ime":"Dzenan",
    "prezime":"Kosuta",
    "godina_rodjenja":1996,
    "broj_indeksa":119141,
    "naziv_fakulteta":"DUNP"
}
student2 = dict(student)
print(student2)
student2["broj_indeksa"] = 256325
print(student2)
print(student)

# Nested (ugnjezdeni) recnici
# Dozvoljeno je unutar nekog recnika kao vrednost staviti novi recnik.
student = {
    "ime":"Dzenan",
    "prezime":"Kosuta",
    "godina_rodjenja":1996,
    "broj_indeksa":119141,
    "fakultet": {"naziv":"DUNP", "lokacija":"Vuka Karadzica 49", "ocenjen": 6.7},
    "ocene_prema_godinama": [7,8,6,9]
}
print(student)

