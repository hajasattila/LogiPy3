path = "utca.txt"
epitmenyek = []
with open(path, "r+", encoding="utf8") as file:
    adok = file.readline().strip().split()
    adosavok = {
        'A': int(adok[0]),
        'B': int(adok[1]),
        'C': int(adok[2])
    }
    for i in file:
        adatok = i.strip().split()
        epitmeny = {
            'adoszam': int(adatok[0]),
            'utca': adatok[1],
            'hazszam': adatok[2],
            'adosav': adatok[3],
            'terulet': int(adatok[4])
        }
        epitmenyek.append(epitmeny)

print(f"2. feladat. A mintában {len(epitmenyek)} telek szerepel.")

print("3. feladat")
szamlalo = 0
adobe = int(input("Add meg egy tulajdonos számát: "))
for i in epitmenyek:
    if adobe == i["adoszam"]:
        print(i["utca"], i["hazszam"])
        szamlalo += 1
if szamlalo == 0:
    print("Nem szerepel az adatállományban")

# feladat 4: //TODO:


def ado(adosonknet, adosav, alapterulet):
    adoszamol = alapterulet * adosonknet[adosav]
    if adoszamol < 10000:
        return 0
    else:
        return adoszamol


# feladat 5:fapados
""" atelek = 0
btelek = 0
ctelek = 0
aosszeg = 0
for i in epitmenyek:
    if i["adosav"] == "A":
        atelek += 1

    elif i["adosav"] == "B":
        btelek += 1

    elif i["adosav"] == "C":
        ctelek += 1

print(atelek)
print(btelek)
print(ctelek) """

# feladat 5 másképp
osszesit = {'A': [0, 0],
            'B': [0, 0],
            'C': [0, 0],
            }
for i in epitmenyek:
    osszesit[i["adosav"]][0] += 1
    osszeg = ado(adosavok, i["adosav"], i["terulet"])
    osszesit[i["adosav"]][1] += osszeg

print("A sávba ", osszesit["A"][0],
      "telek esik, az adó", osszesit["A"][1], "Ft.")
print("B sávba ", osszesit["B"][0],
      "telek esik, az adó", osszesit["B"][1], "Ft.")
print("C sávba ", osszesit["C"][0],
      "telek esik, az adó", osszesit["C"][1], "Ft.")
# FELADAT 6
utcasav = {}
for i in epitmenyek:
    if i["utca"] in utcasav:
        utcasav[i["utca"]].add(i["adosav"])
    else:
        utcasav[i["utca"]] = set(i["adosav"])

print(utcasav)
for i in utcasav:
    if len(utcasav[i]) > 1:
        print(i)
# feladat 7

adoTulajdonosonkent = {}
for i in epitmenyek:
    if i["adoszam"] in adoTulajdonosonkent:
        adoTulajdonosonkent[i["adoszam"]] += ado(adosavok, i["adosav"], i["terulet"])
    else:
        adoTulajdonosonkent[i["adoszam"]] = ado(adosavok, i["adosav"], i["terulet"])

with open("fizetendo.txt", "w+", encoding="utf8") as file:
    for i in adoTulajdonosonkent:
        print(i,adoTulajdonosonkent[i], file=file)
