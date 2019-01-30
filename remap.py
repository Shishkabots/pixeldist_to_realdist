# DO NOT RUN THIS CODE ON IMAGES OTHER THAN CHESSBOARDS (the images would have been deleted, but now they won't be)

import numpy as np
import cv2
import glob
import os

images = glob.glob('*.jpg') # use .png for the result, .jpg for input so calibrated images don't get calibration reapplied

mapx = np.load('mapx_values.npy')
print mapx
mapy = np.load('mapy_values.npy')

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imwrite(fname[:-4] + '_grayscale.png', gray)
    dst = cv2.remap(gray,mapx,mapy,cv2.INTER_LINEAR)

    # crop the image
    #x,y,w,h = roi
    #dst = dst[y:y+h, x:x+w]
    
    cv2.imwrite(fname[:-4] + '_calibrated.png', dst)
