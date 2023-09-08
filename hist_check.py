import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import PIL
from PIL import Image

def validate(imagepath):
    ret = notcorrupted(imagepath)
    if ret == "okay":
        im = cv.imread(str(imagepath))
        # calculate mean value from RGB channels and flatten to 1D array
        vals = im.mean(axis=2).flatten()
        # plot histogram with 255 bins
        b, bins, patches = plt.hist(vals, 255)
        if np.mean(b)/max(b)>0.2:
            "good"
        else:
            "bad"

def notcorrupted(imagepath):
    try:
        im = Image.load(imagepath)
        im.verify() #I perform also verify, don't know if he sees other types o defects
        im.close() #reload is necessary in my case
        im = Image.load(imagepath) 
        im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        im.close()
        return "okay"
    except: 
        return "faulty"