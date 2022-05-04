from mtcnn import MTCNN
import cv2

# import os
# os.environ["CUDA_VISIBLE_DEVICES"]="-1"

def save_face(frame, faces):
    i = 0
    for f in faces:
        x, y, w, h = f["box"]
        i += 1
        crop = frame[y:y+h, x:x+w]
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imwrite(f"./file{i}.png", crop)
    return


# Detect faces in the images
detector = MTCNN()
camera = cv2.VideoCapture(0)

while True:
    ret, img = camera.read()
    if ret:
        # Chuyen gray
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Detect faces in the images
        faces = detector.detect_faces(gray)
        # Draw rectangle around the face
        for f in faces:
            x, y, w, h = f["box"]
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # qroi_color = img[y:y + h, x:x + w]

        cv2.imshow("Picture", img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('s'):
        save_face(img, faces)

camera.release()
cv2.destroyAllWindows()

# 255,0,0 : blue