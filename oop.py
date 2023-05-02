#OOP objektum oriented programming

""" class Szuper(object):
    pass

class Szuperhos():
    pass """

class Szuperhos:              
    #adattag létrehozása és inicializálása

    def __init__(self, nev, szuperero = 50) -> None:
        self._nev = nev          
        self._szuperero = szuperero
        self.kepesegek = []
        print("--- Hős létrehoza ---")

    @property               #get property
    def szuperero(self):
        return self._szuperero
    
    @szuperero.setter       #set property
    def szuperero(self, ertek):
        self._szuperero = ertek

    @property               #get property
    def nev(self):
        return self._nev
    
    @nev.setter       #set property
    def nev(self, ertek) -> str:
        self._nev = ertek

    def __str__(self):
        return (f"{self._nev} egy szuperhős, akinek az ereje: {self._szuperero}")

    #operator overload

    #Ha két szuperhős megegyezik, egy boolt visszaad

    def __eq__(self, masikHos) -> bool:
        return self._nev == masikHos._nev and self._szuperero == masikHos._szuperero
    
    def __add__(self, masikHos):
        if  isinstance(masikHos, Szuperhos):
            ujSzuperero = self._szuperero + masikHos._szuperero
            ujSzuperHos = Szuperhos("Megahős", ujSzuperero)
            return ujSzuperHos
        else:
            print("Hőst, csak hős osztálybelivel lehet összeadni")

    def __iadd__(self, kepesseg):
        if isinstance(kepesseg, str):
            self.kepesegek.append(kepesseg)
            return self
        else:
            print("Csak stringként lehet képességet megadni!")

#Példányok. Amik a szuperhős osztályból származnak.
hos1 = Szuperhos("Hulk", 100)
""" print(hos1) """
hos2 = Szuperhos("Thor", 100)
print(hos1 == hos2)
hos3 = hos1 + hos2
print(hos3)
hos1 += "Repülés"
hos3 += "Vizenjárás"
print(hos1.kepesegek, hos3.kepesegek)
#Láhatóság - getter -> megkapjuk az értékét, setter -> beállítjuk az értékét


#Tipus ellenörzés       isinstance(42, int)
""" print(isinstance(42, int))
print(isinstance("42", str))
print(isinstance(42.0, float))
print(isinstance(42, bool)) """



