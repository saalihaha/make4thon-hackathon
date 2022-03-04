from keras.models import load_model
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np
import os 






def run_classifier(file_):
    current_working_directory = os.getcwd()
    face_classifier = cv2.CascadeClassifier(os.path.join(current_working_directory,"haarcascade_frontalface_default.xml"))
    classifier =load_model(os.path.join(current_working_directory,"model.h5"))

    emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

    # frame = cv2.imread(os.path.join(current_working_directory,"images","4.png"))
    frame = cv2.imread(file_)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray)

        
    for (x,y,w,h) in faces:   
        roi_gray = gray[y:y+h,x:x+w]
        roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)



        if np.sum([roi_gray])!=0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi,axis=0)

            prediction = classifier.predict(roi)[0]
            label=emotion_labels[prediction.argmax()]
            print(label)
            return label
            
     

if __name__=='__main__':
    print("hello")