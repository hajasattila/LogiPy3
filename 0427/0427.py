# Feladat 1 - File megnyitása
dinamikus = 'script.txt'  # stringként a file nevét eltáráoljuk
# fügvénnyel beolvassuk a filet, majd megmondjuk milyen műveletet végzünk (w,r,a)
# Milyen encoding-ot használunk(van-e, nincs-e ékezet)


def openFile():
    f = open(dinamikus, 'r', encoding='utf8')
    print(f.read())
    f.close()
# openFile()
# Feladat - 1.b: keressünk meg karaktereket a szövegben


def openFileChar():
    file = open(dinamikus, 'r', encoding='utf8')
    print(file.read(6))
    file.seek(10)
    print(file.read(6))
    file.seek(0)
    print(file.read(6))
    file.close()  # Biteket szabadit fel, több ram, gyorsabb futás
# openFileChar()
# Feladat 2 - Sorok beolvasása


def openLines():
    file = open(dinamikus, 'r', encoding='utf8')
    sorok = file.readlines()
    for i in sorok:
        print(i[0])
    file.close()
# openLines()
# Feladat 3 - Szöveg keresése


def findText():
    with open(dinamikus, encoding="UTF-8") as f:
        if "LogiScool" in f.read():
            print("Valamiért megtaláltuk azt, hogy LogiScool")
        else:
            print("Ez a szöveg, még mindig a HarryPotterről szól")
findText()
