import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Model
import os
import numpy as np
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
tf.__version__




trained_model = load_model('model/blur/blur_detect.h5') 
glareCNN = tf.keras.models.load_model('model/glare/glare_detect.h5')
source_dir = "C:\\Users\\trade\\OneDrive\\Documents\\GitHub\\pretrained-image-quality-cnn\\all_images\\"

 

buffr_blur = []
score_blur = []
pred_blur = []


buffr_glare=[]
pred_glare=[]
score_glare=[]

name=[]

image_array=[]
for i in os.listdir(source_dir):

    #blur check 
    img = tf.keras.preprocessing.image.load_img(source_dir+i,target_size = (128,128))
    x = tf.keras.preprocessing.image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    
    image_array.append(x)
    
    classes = trained_model.predict(x/255)
    buffr.append(img)
    score_blur.append(classes)
    name.append(i)
    if classes[0][0]<0.9:
        pred_blur.append("blur")
    else:
        pred_blur.append("not blur")


     #glare check    
    test_image1 = tf.keras.preprocessing.image.load_img(source_dir+i, target_size = (64,64))
    test_image2 = tf.keras.preprocessing.image.img_to_array(test_image1) #convert PIL image to array
    test_image2 = np.expand_dims(test_image2, axis = 0) #expand image dimensions to make it compatible with CNN input
    glare = glareCNN.predict(test_image2/255) #Values in the array scaled from [0,255] -> [0,1]

    score_glare.append(glare)
    if glare[0][0] <0.6: #CNN model refers to 0 as "glare" and 1 as "not glare", applying a threshold for both cases.
        pred_glare.append("Glare")
    else:
        pred_glare.append("Not Glare") #values greater than 0.5