#  1. Napraviti funkciju koja vraca povrsinu pravougaonika na osnovu unetih argumenata. 
#    Odnosno povrsinu kvadrata ako su dva data argumenta jednaka.

#  2. Napraviti funkciju koja pretvara broj incha u cm.
#     Pozivanjem funkcije treba uneti broj incha. 

# 1.

def povrsina(a,b):
    if a == b:
        return f"Povrsina kvadrata je {a*b}."
    return f"Povrsina pravougaonika je {a*b}"

print(povrsina(4,6))
print(povrsina(7,7))

# 2.

def to_cm(inch):
    return f"Broj centimetara na osnovu unetih incha je: {inch * 2.54}."

print(to_cm(45))