#  Bolji u dve discipline.

hana_mat = int(input("Unesite Hanin broj osvojenih poena iz matematike: "))
hana_prog = int(input("Unesite Hanin broj osvojenih poena iz programiranja: "))
seid_mat = int(input("Unesite Seidov broj osvojenih poena iz matematike: "))
seid_prog = int(input("Unesite Seidov broj osvojenih poena iz programiranja: "))

hana_ukupno = hana_mat + hana_prog
seid_ukupno = seid_mat + seid_prog

if hana_ukupno > seid_ukupno:
    print(1)
elif hana_ukupno < seid_ukupno:
    print(2)
elif hana_ukupno == seid_ukupno:
    if hana_prog > seid_prog:
        print(1)
    elif hana_prog < seid_prog:
        print(2)
    else:
        print(1)
