import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
dinamikus = 'deniroo.csv'    # egymástól föggően hol találkozhatnak


# feladat - 1 Nyissujk meg a csv filet és írjuk ki az adatait


def opencsv():
    csvfile = open(dinamikus)
    data = csv.reader(csvfile, skipinitialspace=True)
    for i in data:
        print(', '.join(i))
    csvfile.close()

# opencsv()

# Feladat - 2: Formázzuk meg a táblát


def openstable():
    pd.set_option("display.max_rows", None)
    file = pd.read_csv(dinamikus, skipinitialspace=True, index_col="Title")
    print(file)


# openstable()
# Feladat 3 - Reindexuljuk a filet
def pickColumns(col):
    pd.set_option("display.max_rows", None)
    file = pd.read_csv(dinamikus, skipinitialspace=True, usecols=col)
    print(file)
#pickColumns(["Score" , "Title", "Year"])

# Feladat 4- Listázzuk ki a column neveket


def columnNames():
    file = pd.read_csv(dinamikus, skipinitialspace=True)
    listOfNames = list(file.columns)
    print(f"A nevei a columnnak: {listOfNames}")


columnNames()

# Feladat 5 - Deniro legjobb filmje!


def bestMovie():
    file = pd.read_csv(dinamikus, skipinitialspace=True,
                       usecols=["Score", "Title"])
    maxScore = max(file["Score"])
    myRow = file[file["Score"] == maxScore]
    print(
        f"A legjobb film: {myRow.iloc[0,1]}, és annak pontja {myRow.iloc[0,0]}")


bestMovie()

# Feladat 6- Deniro legrosszabb filmje!


def worstMovie():
    file = pd.read_csv(dinamikus, skipinitialspace=True,
                       usecols=["Score", "Title"])
    minScore = min(file["Score"])
    myRow = file[file['Score'] == minScore]
    print(
        f"A legrosszabb film {myRow.iloc[0,1]}, és annak a pontja {myRow.iloc[0,0]}")


worstMovie()

# Feladat 7 - A filmek átlagospontja


def avarage():
    file = pd.read_csv(dinamikus, skipinitialspace=True,
                       usecols=["Score"])
    avg = 0
    for i in file['Score']:
        avg += i
    avg /= len(file["Score"])
    print(f"Az átlagos pont {round(avg)}")


avarage()

# Feladat 8 - plot érték


def plotdata():
    file = pd.read_csv(dinamikus, skipinitialspace=True,
                       usecols=["Year", "Score"])
    file.plot(x="Year", y='Score', kind='scatter')
    plt.title("Év-Pont gráf")
    plt.show()


# plotdata()

def plotdatacurve():
    file = pd.read_csv(dinamikus, skipinitialspace=True,
                       usecols=["Year", "Score"])
    x = np.array(file['Year'])
    y = np.array(file['Score'])
    temp = np.polyfit(x, y, 10)
    poly = np.poly1d(temp)
    newX = np.linspace(x[0], x[-1])
    newY = poly(newX)
    plt.plot(x, y, "o", newX, newY)
    plt.xlim([x[0]-1, x[-1]+1])
    plt.title("Év-Pont gráf")
    plt.savefig("myPlot.jpg")
    plt.show()


# plotdatacurve()


nevek = ['Andor', 'Bori', 'Csilla', 'Dénes']
eletkor = [10, 8, 22, 57]
magassag = [140, 130, 170, 185]
telepules = ["Cegléd", "Abony", 'Kőrős', 'Szeged']
Adatsor = list(zip(nevek, eletkor, magassag, telepules))
#print(Adatsor, "\n")
df1 = pd.DataFrame(data=Adatsor, columns=[
                   'Név', 'Eletkor', 'Magassag', 'Telepules'])
print(df1)