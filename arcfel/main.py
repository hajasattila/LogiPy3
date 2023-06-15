import cv2
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox

# Load the cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def resize_img(img):
    # Get the dimensions of the input image
    height, width, _ = img.shape

    # Calculate the maximum dimensions to resize the image to
    max_dim = 600
    resized_width = max_dim
    resized_height = max_dim

    # If the width is greater than the height, then resize the width
    if width > height:
        resized_height = int(max_dim * height / width)
    # If the height is greater than the width, then resize the height
    else:
        resized_width = int(max_dim * width / height)

    # Resize the image to the maximum dimensions
    resized_img = cv2.resize(img, (resized_width, resized_height))

    return resized_img


def detect_faces():
    # Open a file selection dialog and get the selected file's path
    file_path = filedialog.askopenfilename()

    file_ext = file_path.split('.')[-1]

    # Check if the file extension is JPG or PNG
    if file_ext.lower() not in ['jpg', 'png']:
        # If the file extension is not JPG or PNG, show an error message
        messagebox.showerror('HIBA', 'Rossz formátum')
        return

    # Read the input image
    img = cv2.imread(file_path)

    # Resize the image to a maximum of 600x600
    img = resize_img(img)

    # Convert the input image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the input image
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Loop over the detected faces
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the output image
    cv2.imshow('Arcfelismerés', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def detect_faces_video():
    # Open a file selection dialog and get the selected file's path
    file_path = filedialog.askopenfilename()

    file_ext = file_path.split('.')[-1]
    # Read the input image or video
    cap = cv2.VideoCapture(file_path)

    # Check if the input is a video
    if cap.isOpened():
        # Loop over the frames of the video
        while True:
            # Read the next frame
            ret, frame = cap.read()

            # Check if the video has ended
            if not ret:
                break

            # Resize the frame to a maximum of 600x600
            frame = resize_img(frame)

            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the frame
            faces = face_cascade.detectMultiScale(gray, 1.1, 8)

            # Loop over the detected faces
            for (x, y, w, h) in faces:
                # Draw a rectangle around the face
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Display the output frame
            cv2.imshow('Arcfelismerés', frame)

            # Check if the user has pressed the `Esc` key
            key = cv2.waitKey(1)
            if key == 27:
                break

        # Release the video capture object and close all windows
        cap.release()
        cv2.destroyAllWindows()
    else:
        messagebox.showerror('HIBA', 'Rossz formátum')
        return


def faceReco():

    # Start capturing video from the webcamera
    video_capture = cv2.VideoCapture(0)

    # Create a Haar Cascade object for face detection
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Loop indefinitely
    while True:
        # Read the current frame from the video capture
        ret, frame = video_capture.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the current frame
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Draw a rectangle around each detected face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Show the current frame in the named window
        cv2.imshow("Arc érzékelés", frame)

        # Wait for a key press
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    video_capture.release()

    # Destroy all windows
    cv2.destroyAllWindows()


# Create the main window
window = tk.Tk()


# Set the window title
window.title('Arcfelismerés')

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the position to start the window in the center of the screen
x_pos = (screen_width // 2) - 300
y_pos = (screen_height // 2) - 200

# Set the window size and position
window.geometry(f'300x75+{x_pos}+{y_pos}')

# Create a button to select an image
btn = tk.Button(text='Válassz képet!', command=detect_faces)
btn.pack(side="top")

# Create a button to select an video
btn_video = tk.Button(text='Válassz videót!', command=detect_faces_video)
btn_video.pack(side="top")

# Create a button to select an camera
btn_camera = tk.Button(text='Saját kamera!', command=faceReco)
btn_camera.pack(side="top")

# Run the main loop

window.mainloop()
