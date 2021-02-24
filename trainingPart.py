import cv2
from PIL import Image
import numpy as np
import os
import pickle



def training_lbph():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR, "TrainingImages")
    face_cascade = cv2.CascadeClassifier("assets/haarcascade_frontalface_default.xml")
    recognizer = cv2.face.LBPHFaceRecognizer_create()


    current_id = 0
    label_ids = {}
    y_labels = []
    x_train = []
    # print(os.walk(image_dir))
    # <generator object _walk at 0x000001AD08533660>
    print(next(os.walk(image_dir)))
    print(next(os.walk(image_dir)))
    print(next(os.walk(image_dir)))
    print(next(os.walk(image_dir)))
    for root, dirs, files, in os.walk(image_dir):
        # print(root)
        # C:\Users\SUDIP\pythonPrograms\FaceRecognizer\TrainingImages
        # print("dir:", dirs)
        # dir: ['Aman Shrestha(7)', 'Aman(07)', 'Sudip paudyal(84)']
        print(files)
        print("hhh")
        for file in files:
            if file.endswith('png') or file.endswith('jpg') or file.endswith("jpeg"):
                path = os.path.join(root, file)

                # print(path) gives absolute path of each image
                label = os.path.basename(root).replace(" ", "-").lower()
                print("label: ", label)
                print("jjj")
                # print(label) root basename in this case is emilia clarke and peter dinklage
                #  now lets add peter-dinklage and emilia-clarke with no duplication
                # print(label)
                if not label in label_ids:
                    label_ids[label] = current_id
                    current_id += 1
                # print(label_ids) {'emilia-clarke': 0, 'peter-dinklage':1}
                id_ = label_ids[label]
                # print(id_) gives id as in 0 or 1
                pil_image = Image.open(path).convert('L')
                # directly converts to grayscale pil_image is actually the grayscale image not pixel intenity
                # size = (100, 100)
                # final_image = pil_image.resize(size, Image.ANTIALIAS)
                # print(final_image)
                #  Antialias refers to reducing distortion while converting high resolution image to low
                image_array = np.array(pil_image, 'uint8')
                # print(image_array.shape)
                #             # print(image_array) numpy array in grayscale
                #             faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
                #             for (x, y, w, h) in faces:
                #                 cv2.rectangle(image_array, (x, y), (x+w, y+h), (0, 255, 0),3 )
                #
                #                 roi = image_array[y:y + h, x:x + w]
                #                 # roi = cv2.resize(roi, (100, 100)) roi is cropped image after face detection
                #                 # print(roi.shape)
                #                 # im = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
                #                 # plt.imshow(im)
                #                 # plt.show()
                #
                #
                #
                print(path)
                print(id_)

                x_train.append(image_array)
                y_labels.append(id_)
                #  This is visualization bits we can delete it
                i = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
                #plt.imshow(i)
                #plt.show()
                # upto here
            #
            #
            #
            # # print(x_train)   contains the list of numpy array of detected cropped faces
            # # print(len(x_train))
            # # print(y_labels)  contains the label of detected face corresponding to x_train
            # # print(len(y_labels))
            # # lets examine the first data from set x_train
            # # analyze = x_train[0]
            # # print(analyze.shape)
            # # print(analyze[150])  # lets check the data in 150th row
            #
            # #[  0   0   0 191 191 191 192 194 194 194 193 193 193 194 194 194 194 194
            # #perfectly fine
            #

    with open("labels.pickle", 'wb') as f:
        pickle.dump(label_ids, f)
    #
    print(len(y_labels))
    print(len(x_train))
    recognizer.train(x_train, np.array(y_labels))
    # # print(help(recognizer.train))
    recognizer.save("trainner.yml")
    print("Trained")
            #
            #
            #     # print(root, dirs, files)
            # # C:\Users\aman1\minor project jupyter\Face recog 1\TrainingData ['Emilia Clarke', 'Peter Dinklage'] []
            # # C:\Users\aman1\minor project jupyter\Face recog 1\TrainingData\Emilia Clarke [] ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg']
            # # C:\Users\aman1\minor project jupyter\Face recog 1\TrainingData\Peter Dinklage [] ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']