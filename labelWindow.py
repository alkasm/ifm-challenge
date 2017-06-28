import cv2
import numpy as np
import labelFinder



__author__ = 'Alexander Reynolds'
__email__ = 'ar@reynoldsalexander.com'



"""Global variable"""



REDISPLAY = False



"""Private helper functions"""



def __set_redisplay(x):
    """Called whenever a trackbar position is moved.
    
    Sets the global variable REDISPLAY to True.
    """
    global REDISPLAY
    REDISPLAY = True


def __initialize_sliders(window_name):
    """Initializes the trackbars"""
    
    # Define trackbar names (NOTE: see trackbar bug under known issues in README
    bar_start = [3,80,20,20]
    bar_end = [10,100,100,50]
    bars = ['Text Dilation Iterations','Sensitivity','Label Size (w*h)','Label Radius']
    for i in range(0,4):
        cv2.createTrackbar(bars[i], window_name, bar_start[i], bar_end[i], __set_redisplay)
    return bars



"""Main public function"""



def display(img):
    """Public function to display the image and color thresholding trackbars."""

    # initialize window and trackbars
    window = 'Annotated Image'
    cv2.namedWindow(window, cv2.WINDOW_NORMAL)
    cv2.namedWindow(window, cv2.WINDOW_NORMAL)
    sliders = __initialize_sliders(window)

    # initializations
    h, w = img.shape[:2]

    dilate_iters = cv2.getTrackbarPos(sliders[0], window)
    s = cv2.getTrackbarPos(sliders[1], window)+155
    label_size = cv2.getTrackbarPos(sliders[2], window)/1000
    radius = cv2.getTrackbarPos(sliders[3], window)
    max_label_size = h * w * label_size
    min_label_size = max_label_size/16

    annotated_img, label_locations = labelFinder.findLabelsApprox(img, 
        dilate_iters, s, min_label_size, max_label_size, radius)

    global REDISPLAY

    # display window with trackbar values that can be changed
    print('Exit with [q] or [esc].')
    while(True):

        # display the image
        REDISPLAY = False
        cv2.imshow(window, annotated_img)
        k = cv2.waitKey(200) & 0xFF # large wait time to remove freezing
        if k == 113 or k == 27:
            break

        # get positions of the sliders
        dilate_iters = cv2.getTrackbarPos(sliders[0], window)
        s = cv2.getTrackbarPos(sliders[1], window)+155
        label_size = cv2.getTrackbarPos(sliders[2], window)/1000
        radius = cv2.getTrackbarPos(sliders[3], window)
        max_label_size = h * w * label_size
        min_label_size = max_label_size/8

        # update contours
        if REDISPLAY:
            annotated_img, label_locations = labelFinder.findLabelsApprox(img, 
                dilate_iters, s, min_label_size, max_label_size, radius)    


    label_annotated_img = img.copy()
    for loc in label_locations:
        x1, y1, x2, y2 = loc
        label = img[y1:y2, x1:x2]
        annotated_label, exact_pos, theta, perimeter, area = labelFinder.findLabelExact(label, loc, 
            s, min_label_size, max_label_size)
        label_annotated_img[y1:y2, x1:x2] = annotated_label

    cv2.destroyWindow(window)
    cv2.imshow(window, label_annotated_img)
    cv2.waitKey(0)
    cv2.destroyWindow(window)

    return label_annotated_img, label_locations