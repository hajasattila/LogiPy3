import cv2
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def resizeImg(img, maximum):
    # Dimenson lekérdezés
    height, width, _ = img.shape
    resizedWidth = maximum
    resizedHeight = maximum
    # Ha a szélesség, vagy a a magasság, magyobb, mit amit megengedtünk, akkor változtassa vissza a méreteket
    if width > height:
        resizedHeight = int(maximum * height / width)
    else:
        resizedWidth = int(maximum * width / height)
    # magát az img-t is ekkorává kell tenni
    resImg = cv2.resize(img, (resizedHeight, resizedWidth))
    return resImg


def detectFaces():
    # File megnyitást végezzen a gombunk
    filePath = filedialog.askopenfilename()
    # Biztos képeket töltünk fel, ellenőrizzök le    asd.jpg
    fileExt = filePath.split('.')[-1]  # Pont utáni részt nézi meg

    if fileExt.lower() not in ['jpg', 'png']:
        messagebox.showerror('HIBA', 'Nem megfelelő formátum')
        return

    try:
        img = cv2.imread(filePath)
        # TODO: resize fügvény megírása 600x600
        img = resizeImg(img, 100)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Találjuk meg az arcokat a feltöltött képen
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Ezzel rajzoljuk meg a négyzetet
        for(x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Displayeljuk az output imaget
        cv2.imshow('Arc felismeres', img)
        cv2.waitKey()
        cv2.destroyAllWindows()
    except:
        messagebox.showerror('HIBA', 'Nem találtam egy arcot sem')


def detectVideo():
    filePath = filedialog.askopenfilename()
    fileExt = filePath.split('.')[-1]
    # Olvassul be az input videót
    cap = cv2.VideoCapture(filePath)
    # Megnézzük az input egy videó-e
    try:
        if cap.isOpened():
            # Loopoljukát a frameket a videóban
            while True:
                ret, frame = cap.read()
                # Megnézzük a videónakmikor van vége.
                if not ret:
                    break
                # Megint használjuk a resize külső függvényt, amit mi hoztunk létre
                frame = resizeImg(frame)

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # DETEKTELJÜK AZ ARCOKAT
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)
                for(x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.imshow('Arcfelismerés',frame)
                #Megvárjuk bezárjuk a programot - esc gombot jelöli majd
                key = cv2.waitKey(1)
                if key == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
    except:
        messagebox.showerror('HIBA', 'Nem találtam egy arcot sem')

def webcam():
    # Kezdjük el capturölni a kamerát a gépnek
    videoCapture = cv2.VideoCapture(0)
    # Új cascade objektum, hogy a capturelt képet feldolgozzuk
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    while True:
        # A jelenlegi framet(fps-t) beolvassuk a videóról.
        ret, frame = videoCapture.read()

        # Convertáljuk át 'grayscale'-é
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Az 'arcokat' felfedjük
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for(x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('Arc érzékelése', frame)

        # Specifikus gombbal lépnük ki
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    # Ha vége a loopnak, akkor bezárunk minden a mainon kívül
    videoCapture.release()
    cv2.destroyAllWindows()


# Készítsünk egy main windows-t
window = tk.Tk()

# Cím beállítása
window.title("Arc felismerés")

# Screen méret
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

# A windows kezdőpozíció
xPos = (screenWidth // 2) - 300
yPos = (screenHeight // 2) - 200
# Az eddig létrehozott változókat berállítjuk
window.geometry(f'300x75+{xPos}+{yPos}')

# Gomb, amivel a képet kiválaszthatjuk a gépről
btn = tk.Button(text="Válassz képet!", command=detectFaces)
btn.pack(side='top')

# Gomb, amivel a videó kiválaszthatjuk a gépről
btn1 = tk.Button(text="Válassz videót!", command=detectVideo)
btn1.pack(side='top')

# Gomb, amivel a webkamera kiválaszthatjuk a gépről
btn2 = tk.Button(text="Saját kamera!", command=webcam)
btn2.pack(side='top')

# X-Y letiltása
window.resizable(False, False)

# Futtassuk a main loopot
window.mainloop()
