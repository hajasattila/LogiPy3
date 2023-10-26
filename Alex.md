# KOLLEKCIÓK
 
uresLista = []
ures1 = list()
 
szamok = [9, 12, 40, 20, 77, 30, 30, 30, 30, 30, 30, 30, 30, 30]
print(szamok)
# Length ~ hossz. len(szamok)
print(len(szamok))
haziAllatok = ["Ubul", "Scooby Doo", "Mikey"]
print(haziAllatok)
print(len(haziAllatok))
 
# Konkrétan egy-egy elemre is tudok hivatkozni! INDEX-ELÉS
print(haziAllatok[1])
print(haziAllatok[-1])
 
gyumolcsok = ["AlMa", "NarAncs", "Korte", "DiNnye", "NektaRin", "", "Kiwi"]
print(len(gyumolcsok))
print(gyumolcsok[4])
print(gyumolcsok[0:3])
print(gyumolcsok[::-1])
#TODO: MEGFORDÍTJUK MINDJÁRT EZEKET AZ ELEMEKET
gyumolcsok[5] = "SargaDinnye"
print(gyumolcsok)
 
for i in gyumolcsok:
    if  i == "SargaDinnye":
        print("Nem szeretem ezt a gyümit")
    else:
        print("Ezt szeretem")
       
for i in gyumolcsok:
    print(i)
   
for i in gyumolcsok:
    i = i.upper()
   
 
for i in gyumolcsok:
    i = i.lower()
    print(i)
 
gyumolcsok = ["AlMa", "NarAncs", "Korte", "DiNnye", "NektaRin", "ASD", "Kiwi"]
# Minden második betút nagyítsuk fel!
for i in range(len(gyumolcsok)):
    new_gyumolcs = ""
    for j in range(len(gyumolcsok[i])):
        if j % 2 == 0:
            new_gyumolcs += gyumolcsok[i][j].lower()
        else:
            new_gyumolcs += gyumolcsok[i][j].upper()
    gyumolcsok[i] = new_gyumolcs
    print(gyumolcsok[i])
 
szuperHos1 = ["Szuperman", "Batman", "Aquamann"]
szuperHos2 = ["Vasember", "Amerikakapitanya", "Hulk"]
 
bosszuAllaok = szuperHos1 + szuperHos2
#Remove eltüntetés
#bosszuAllaok.remove("Szuperman")
print(bosszuAllaok)
#Sort, az a rendezés ABC vagy növekvő sorrend alapján
bosszuAllaok.sort()
print(bosszuAllaok)
 
# Feldarabolunk egy szöveget! TUDUNK SZÉTVÁGNI
szöveg = "A mai napon nagyon sok kalandban vettem resz, es az egyik ilyen a python orank!"
# SPLIT szétdarabolás
 
felvagott = szöveg.split("a") #mit, mit akarunk csinálni vele, minek a minetén darablojuk
print(felvagott)
print(type(szöveg))
print(type(felvagott))
# TUDUNK ÖSSZEFÚZNI IS!
# JOIN join
 
gyumolcsok = ["alma", "korte", "dinnye", "szilva"]
#Mi alapján, mit akarunk csinálni és mit
print(";".join(gyumolcsok))
