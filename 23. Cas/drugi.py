import datetime

trenutno_vreme = datetime.datetime.now()
print(trenutno_vreme)

datum_rodjenja = datetime.datetime(1996, 6, 24, 23, 43, 36)
print(datum_rodjenja)

dan_rodjenja = datum_rodjenja.strftime("%a")
print(dan_rodjenja)

mesec_rodjenja = datum_rodjenja.strftime("%B")
print(mesec_rodjenja)

datum2 = datetime.datetime(2004, 5, 24)
print(datum2)
