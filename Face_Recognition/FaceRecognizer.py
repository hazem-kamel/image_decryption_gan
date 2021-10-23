import dlib
import numpy as np
import sys
import os

def BrowserDataBase(validation_img,file,subdir):
        status = FaceRecognizer(validation_img, subdir+"\\"+file)
        print(status)
        return status



model = dlib.face_recognition_model_v1(sys.path[1]+'\Face_Recognition\dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(sys.path[1] + '\Face_Recognition\shape_predictor_5_face_landmarks.dat')


def FaceRecognizer(image_validation_path, image_db_path):
    # Detection part
    image_to_validate = dlib.load_rgb_image(image_validation_path)
    image_from_db = dlib.load_rgb_image(image_db_path)

    image_valid_segment = detector(image_to_validate, 1)
    image_data_segment = detector(image_from_db, 1)
    print(len(image_valid_segment))
    print(len(image_data_segment))
    if(len(image_data_segment) == 0 or len(image_valid_segment) == 0):
        return False
    image_valid_shape = sp(image_to_validate, image_valid_segment[0])
    image_data_shape = sp(image_from_db, image_data_segment[0])
    image_valid_aligned = dlib.get_face_chip(image_to_validate, image_valid_shape)
    image_data_aligned = dlib.get_face_chip(image_from_db, image_data_shape)

    image_validation = model.compute_face_descriptor(image_valid_aligned)
    image_data = model.compute_face_descriptor(image_data_aligned)

# Check weather we need to scrap the whole Database for similar person Or both images will be uploaded
    image_array_validate = np.array(image_validation)
    image_array_db = np.array(image_data)
    def findEucldianDistance():
        eucldianDistance = image_array_validate - image_array_db
        eucldianDistance = np.sum(np.multiply(eucldianDistance , eucldianDistance))
        eucldianDistance = np.sqrt(eucldianDistance)
        return eucldianDistance
    distance = findEucldianDistance()
    threshold = 0.7
    if distance < threshold:
        return True
    else:
        return False


