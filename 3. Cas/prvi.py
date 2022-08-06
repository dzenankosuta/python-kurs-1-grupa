#  Varijable (NASTAVAK)

#  NAZIV PROMENLJIVE. Pravila:
#  1. Naziv promenljive mora pocinjati ili nekim slovom (A-Z) ili _
#  2. Promenljive u jeziku Python su case sensitive (OSETLJIV je na mala i velika slova)
#  3. Naziv promenljive moze u sebi sadrzati brojeve (Ali ne sme broj biti pocetni karakter promenljive)
#  4. Promenjive koje se sastoje iz vise reci:
#         1. reci mogu biti odvojene _                             => moj_kabinet = ...
#         2. svaka rec pocinje velikim slovom                      => MojKabinet = ...
#         3. posle prve, svaka naredna rec pocinje velikim slovom  => mojKabinet = ...
#  5. PROMENLJIVE KOJE SE SASTOJE IZ VISE RECI MORAJU BITI NAZVANE NEKOM OD GORE NAVEDENIH METODA!!!
#     NE SME SE DESITI DA PROMENLJIVOJ DODELITE VREDNOST A DA IZMEDJU RECI POSTOJI RAZMAK => TO CE REZULTOVATI ERROR
#     TAKODJE NE SME POSTOJATI - IZMEDJU RECI U JEDNOJ PROMENLJIVOJ (moj-kabinet)!!!

kurs = "Kurs programiranja"
print(kurs)
kurs_python = "Kurs programskog jezika Python"
print(kurs_python)

#  kurs-java = "Kurs programskog jezika Java"  Dobili smo error jer smo dodelili naziv koji nije prihvacen

#  kurs java = "Kurs programskog jezika Java" 
#  print(kurs java) Dobili smo error jer smo dodelili naziv koji nije prihvacen

kursJava = "Kurs programskog jezika Java" 
print(kursJava)

KursC =  "Kurs programskog jezika C" 
print(KursC)

kurs2 =  "Kurs nekog novog programskog jezika" 
print(kurs2)