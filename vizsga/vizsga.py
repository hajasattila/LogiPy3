# TÉMAKÖRÖK
# ALAPOK:

# az egy soros
""" TÖBB
SOROS """

# Mi az az indentálás? -> jó sorrendben, tabolva egymás alatt, minden a megfelelő helyen
# def fugveny():
#   pass
# Jól indentált


def fugveny():
    if True:
        pass
    return


# NEM jól indentált
""" def fugveny():
if True:
pass
return """

# KULCSSZAVAK lesznek:
#print(), sysout(), consol.log()
# def(), definition(), function()

# INTERPETER -> sorrol sorra, sorrendben olvassa, és nem egészben
print("Ez fog először kiiratódni")
print("Ez fog másodszorra kiiratódni")

# COMPILER
# Ember és a gép közötti kommunikációt segíti.
# A magas(emberhez közeli nyelvet) lefordítja egy alacsony(géphez közeli nyelvre)

# Változók:
# string -> szöveg           -> "ez egy string"
# int    -> számok, egész    -> 5
# bool   -> logikai változók -> True/False
# float  -> valós számok     -> 5.0

# Fontos a sorrend, mit miután hozunk létre, ez az interpeter miatt.
# Kívülről befelé tudunk adatot átadni, belülről kifelé, NEM
a = "Ez egy szöveg"
a += "."
print(a)
b = 5
c = 6
d = b + c
print(d)
print(b + c)
print(b - c)
# Maradékos osztás, megmondja mennyi a maradék
print(10 % 3)
# Osztások
# 1.) Elhagyja a tizedes pont utáni értéket. EGÉSZ osztás
print(10 // 3)
# 2.) Nem hagyja el a tizedes pontot
# Kerekítünk .2 -> round((állítás),2)
print(round(10 / 3, 2))
#Deklaráció -> változó létrehozása
a = 5
#Felül deklaráltuk
a = 7
a /= 2
print(a)

#Bitwise operátors:
x = 5
result = ~x
print(result)  # eredmény: -6
