# import cv2
# import os

# # Directory to store user images
# USER_DB = "user_images"
# os.makedirs(USER_DB, exist_ok=True)

# def add_user(user_id):
#     """Capture images for a new user and save them."""
#     cap = cv2.VideoCapture(0)
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#     print(f"Adding new user: {user_id}")
#     user_path = os.path.join(USER_DB, user_id)
#     os.makedirs(user_path, exist_ok=True)

#     frame_count = 0
#     saved_images = 0

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to capture frame.")
#             break

#         # Detect faces using OpenCV Haar Cascade
#         gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#         faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

#         for (x, y, w, h) in faces:
#             # Draw rectangle around face
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

#             # Save every 30th frame with detected face
#             if frame_count % 30 == 0:
#                 face_img = frame[y:y + h, x:x + w]
#                 face_path = os.path.join(user_path, f"face_{saved_images}.jpg")
#                 cv2.imwrite(face_path, face_img)
#                 print(f"Saved image: {face_path}")
#                 saved_images += 1

#         frame_count += 1

#         # Show video feed
#         cv2.imshow("Add User - Press 'q' to stop", frame)

#         # Exit when 'q' is pressed or 5 images are saved
#         if cv2.waitKey(1) & 0xFF == ord('q') or saved_images >= 5:
#             break

#     cap.release()
#     cv2.destroyAllWindows()
#     print(f"User {user_id} added successfully.")


# if __name__ == "__main__":
#     user_id = input("Enter new user ID: ")
#     add_user(user_id)


import cv2
import os

# Directory to store user images
USER_DB = "user_images"
os.makedirs(USER_DB, exist_ok=True)

def user_exists(user_id):
    """Check if a user directory already exists."""
    return os.path.exists(os.path.join(USER_DB, user_id))

def add_user(user_id):
    """Capture images for a new user and save them."""
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    print(f"Adding new user: {user_id}")
    user_path = os.path.join(USER_DB, user_id)
    os.makedirs(user_path, exist_ok=True)

    frame_count = 0
    saved_images = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame.")
            break

        # Detect faces using OpenCV Haar Cascade
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

        for (x, y, w, h) in faces:
            # Draw rectangle around face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Save every 30th frame with detected face
            if frame_count % 30 == 0:
                face_img = frame[y:y + h, x:x + w]
                face_path = os.path.join(user_path, f"face_{saved_images}.jpg")
                cv2.imwrite(face_path, face_img)
                print(f"Saved image: {face_path}")
                saved_images += 1

        frame_count += 1

        # Show video feed
        cv2.imshow("Add User - Press 'q' to stop", frame)

        # Exit when 'q' is pressed or 5 images are saved
        if cv2.waitKey(1) & 0xFF == ord('q') or saved_images >= 5:
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"User {user_id} added successfully.")

if __name__ == "__main__":
    user_id = input("Enter new user ID: ")
    
    # Check if user already exists
    if user_exists(user_id):
        print(f"User ID '{user_id}' already exists. Please use a different ID.")
    else:
        add_user(user_id)
