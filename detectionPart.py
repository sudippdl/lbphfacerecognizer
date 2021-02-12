# imports
import os
import cv2
import time

# Base directory of our project ....\FaceRecognizer
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# make directory for training images if it doesn't exist
if not os.path.exists("TrainingImages"):
    os.makedirs('TrainingImages')


def capture(name, idd):
    """

    :param name: Name of student
    :param idd: unique id for each entry
    :return: None
    """
    sample = 0
    training_image_directory = os.path.join(BASE_DIR, "TrainingImages")
    # our classifier object
    face_cascade = cv2.CascadeClassifier("assets/haarcascade_frontalface_default.xml")
    # generate unique directory
    name_id = name + "(" + str(idd) + ")"
    print(f"System taking sample picture for {name_id}!!\n")
    id_path = training_image_directory + os.sep + name_id
    # id_path is directory belonging to each entry to store sample images
    # make directory if not exists
    if not os.path.exists(id_path):
        os.makedirs(id_path)
    # video object 0 => primary camera
    video = cv2.VideoCapture(0)
    time.sleep(2)
    if not video.isOpened():
        raise IOError("cannot open webcam")
    # capture images until sample=60
    while True:
        _, frame = video.read()
        # gray frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=25)
        if len(faces) > 0:
            for x, y, w, h in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                sample += 1
                cropped_gray = gray[y: y + h, x: x + w]
                resized_gray = cv2.resize(cropped_gray, (100, 100))
                cv2.imshow("new", resized_gray)
                cv2.imwrite(id_path + os.sep + str(sample) + ".jpg", resized_gray)
        cv2.imshow("Input", frame)
        c = cv2.waitKey(1)
        if c == 27:
            break
        if sample > 59:
            break

    video.release()
    cv2.destroyAllWindows()
    print("done")


def user_input():
    name = input("Enter full Name")
    while True:
        try:
            unique_id = int(input("Enter numeric unique id:\t"))
        except:
            print("Id must be numeric: \t")
        else:
            break
    print("System taking pictures of you.Please smile :) \n")
    capture(name, unique_id)


user_input()
