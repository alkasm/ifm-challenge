import cv2
import numpy as np
import labelFinder



__author__ = 'Alexander Reynolds'
__email__ = 'ar@reynoldsalexander.com'



# read image
img = cv2.imread('data/lowres.jpg')
h, w = img.shape[:2]

# parameters
sensitivity = 220
label_size_percentage = 0.04
radius = 30
dilate_iterations = 3

max_label_size = h * w * label_size_percentage
min_label_size = max_label_size/16

annotated_img, label_locations = labelFinder.findLabelsApprox(img, 
    dilate_iterations, sensitivity, min_label_size, max_label_size, radius)

cv2.imshow('Annotated Image', annotated_img)
cv2.waitKey(0)

label_annotated_img = img.copy()
i = 0
for loc in label_locations:
    x1, y1, x2, y2 = loc
    label = img[y1:y2, x1:x2]
    annotated_label, exact_pos, theta, perimeter, area = labelFinder.findLabelExact(label, loc, 
        sensitivity, min_label_size, max_label_size)
    label_annotated_img[y1:y2, x1:x2] = annotated_label
    print('### LABEL %d ###' % i,
        '\nPosition: ', exact_pos,
        '\nOrientation: ', theta,
        '\nPerimeter:', perimeter,
        '\nArea:', area, '\n')
    i += 1

cv2.imshow('Annotated Labels', label_annotated_img)
cv2.waitKey(0)