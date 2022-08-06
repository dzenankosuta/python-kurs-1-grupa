# Domaci:
# 1. Zadatak:
#  Prosli domaci zadatak odraditi preko jedne print metode, koristeci \n escape karakter.
# 2. Zadatak:
#  Napraviti funkciju gde korisnik unosi dve recenice. Nakon toga ispisati sledece:
#  Duzinu prve i druge recenice,
#  duzinu prve i druge recenice bez eventualnih razmaka na krajevima recenica,
#  prvu recenicu gde zelimo da zamenimo svaki "a" karakter sa "b" karakterom,
#  drugu recenicu gde zelimo da zamenimo svaki niz karaktera "raspust" sa 
#  nizom karaktera "letnji raspust",
#  prvu i drugu recenicu podeljenu na svaki zarez.

# 1.
def funkcija():
    recenica = str(input("- "))
    print(f"{recenica.upper()}\n{recenica.lower()}\n{len(recenica)}")

funkcija()

# 2.
def funkcija2():
    recenica1 = str(input("Unesite prvu recenicu: "))
    recenica2 = str(input("Unesite drugu recenicu: "))
    print(f"Duzina prve recenice je: {len(recenica1)}")
    print(f"Duzina druge recenice je: {len(recenica2)}")
    print(f"Duzina prve recenice koriscenjem strip() metode iznosi: {len(recenica1.strip())}")
    print(f"Duzina druge recenice koriscenjem strip() metode iznosi: {len(recenica2.strip())}")
    print(recenica1.replace("a", "b"))
    print(recenica2.replace("raspust", "letnji raspust"))
    print(recenica1.split(", "))
    print(recenica2.split(", "))

funkcija2()