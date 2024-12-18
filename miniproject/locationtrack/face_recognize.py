import cv2
import os
import numpy as np
import threading
from tkinter import Tk, Button, Label, StringVar, Entry, Toplevel
from deepface import DeepFace
from add_user import add_user, USER_DB
from PIL import Image, ImageTk
from scipy.spatial.distance import cosine

def verify_user(frame, user_id):
    """Verify if the given frame matches the stored images of the user."""
    user_path = os.path.join(USER_DB, user_id)
    if not os.path.exists(user_path):
        print(f"User {user_id} not found.")
        return False

    # Extract the embeddings of the live frame
    try:
        live_embedding = DeepFace.represent(frame, model_name='VGG-Face', enforce_detection=False)
    except Exception as e:
        print(f"Error extracting live face embedding: {e}")
        return False

    live_embedding = live_embedding[0]['embedding']  # Extract the embedding

    for img_name in os.listdir(user_path):
        img_path = os.path.join(user_path, img_name)
        try:
            # Extract the embedding of the stored image
            stored_embedding = DeepFace.represent(img_path, model_name='VGG-Face', enforce_detection=False)
            
            stored_embedding = stored_embedding[0]['embedding']  # Extract the embedding
            
            # Compare the embeddings using cosine similarity (cosine distance)
            distance = cosine(live_embedding, stored_embedding)
            
            # Define a threshold for the distance (lower is better)
            if distance < 0.4:  # You can experiment with this threshold value
                print(f"Face match found for user {user_id} with {img_name}")
                return True
        except Exception as e:
            print(f"Error verifying face for {img_name}: {e}")

    print(f"No match found for user {user_id}.")
    return False

def start_verification_window(user_id):
    """Opens a new window to verify attendance using live webcam feed."""
    verification_window = Toplevel(root)
    verification_window.title(f"Verify Attendance: {user_id}")
    verification_window.geometry("700x500")

    # Create a label in the verification window to display the video
    label = Label(verification_window)
    label.pack()

    # Add a button to stop the webcam feed
    stop_button = Button(verification_window, text="Stop Verification", command=verification_window.quit, width=20)
    stop_button.pack(pady=10)

    def verify_live():
        """Starts webcam feed and verifies face in real time."""
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        face_verified = False

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

            for (x, y, w, h) in faces:
                # Draw rectangle around the face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                face_frame = frame[y:y + h, x:x + w]

                if not face_verified:
                    result = verify_user(face_frame, user_id)
                    if result:
                        face_verified = True
                        cv2.putText(frame, "Verified!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    else:
                        cv2.putText(frame, "Not Verified!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Convert the frame to a format that Tkinter can display
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            img_tk = ImageTk.PhotoImage(image=img)

            # Update the label with the new image
            label.img_tk = img_tk
            label.config(image=img_tk)

            # Stop the verification when 'q' is pressed or face is verified
            if cv2.waitKey(1) & 0xFF == ord('q') or face_verified:
                break

        cap.release()
        cv2.destroyAllWindows()
        verification_window.destroy()

    # Run the live verification in a separate thread to avoid blocking the GUI
    threading.Thread(target=verify_live).start()

def verify_user_gui():
    """Callback for verifying user attendance."""
    user_id = user_id_var.get()
    if not user_id.strip():
        status_var.set("Error: User ID cannot be empty.")
        return

    start_verification_window(user_id)

def add_new_user_gui():
    """Callback for adding a new user."""
    user_id = user_id_var.get()
    if not user_id.strip():
        status_var.set("Error: User ID cannot be empty.")
        return

    user_path = os.path.join(USER_DB, user_id)
    if os.path.exists(user_path):
        status_var.set(f"User ID '{user_id}' already exists.")
        return

    add_user(user_id)
    status_var.set(f"User '{user_id}' added successfully.")

def exit_app():
    """Exit the application."""
    root.destroy()

# Create the main GUI window
root = Tk()
root.title("Face Recognition Attendance System")
root.geometry("400x300")

# User ID Input
Label(root, text="Enter User ID:").pack(pady=5)
user_id_var = StringVar()
Entry(root, textvariable=user_id_var, width=30).pack(pady=5)

# Buttons
Button(root, text="Add New User", command=add_new_user_gui, width=20).pack(pady=10)
Button(root, text="Verify Attendance", command=verify_user_gui, width=20).pack(pady=10)
Button(root, text="Exit", command=exit_app, width=20).pack(pady=10)

# Status Label
status_var = StringVar()
Label(root, textvariable=status_var, wraplength=350, fg="blue").pack(pady=20)

# Start the GUI event loop
root.mainloop()
