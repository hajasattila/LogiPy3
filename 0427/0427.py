# Feladat 1 - File megnyitása
import os
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

# Feladat 4 - File létrehozása


def createFile(filename):
    f = open(filename+'.txt', 'w+', encoding='UTF8')
    f.close()


#myFile = createFile('kecskesajt')

# Feladat 5 - írjunk a fileba!


def writeFile():
    f = open('kecskesajt.txt', 'a+', encoding='UTF8')
    f.write("Szeretem a sajtot")
    f.close()
# writeFile()
# Feladat 6 - copy egy szöveget szóközök nélkül


def removeSpaces():
    f = open(dinamikus, 'r+', encoding='UTF8')
    text = f.read().replace(" ", "")
    g = open("noSpaces.txt", 'w+', encoding='utF-8')
    g.write(text)
    g.seek(0)
    print(g.read())
    f, g.close()


# removeSpaces()
# Saját feladat - 7 : hozzunk létre egy új filet,
# amibe kiírunk annyi számot, amennyit az user beír az inputra!
def oneToX():
    num = int(input("Mennyi számot írjak ki? "))
    f = open("newFile.txt", 'w+', encoding='uTf8')
    for i in range(1, num+1):
        if i % 2 == 0:
            i = "Páros"
        f.write(str(i)+" ")
    f.seek(0)
    f.close()
# oneToX()


def lastLines(n):
    f = open(dinamikus, 'r', encoding='utf8')
    lines = f.readlines()
    while n > 0:
        print(lines[-n], end='')
        n -= 1
    f.close()
# lastLines(2)


def deleteFiles():
    fileName = input("Melyik filet töröljem ki: ")
    try: #Próbálkozunk végfehajtani valami műveletet
        os.remove(fileName + '.txt')
        print(f"Sikeresen törölve {fileName}")
    except: #Ha nem sikerül, akkor ez történjen!
        print("Nincs ilyen filename")
        raise Exception('Nincs ilyen file!') #Saját hiba jelzés!
deleteFiles()
