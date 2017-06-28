import cv2
import numpy as np



__author__ = 'Alexander Reynolds'
__email__ = 'ar@reynoldsalexander.com'



"""Private Helper Functions"""



def __dilateEqualizeGray(img, iters):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((4,5), dtype=np.uint8)
    gray = cv2.dilate(gray, kernel, iterations=iters)
    gray = cv2.equalizeHist(gray)
    gray = cv2.medianBlur(gray, 21)
    return gray


def __threshMask(gray, sensitivity):

    ret, mask = cv2.threshold(gray, sensitivity, 255, cv2.THRESH_BINARY)
    return mask


def __autoMask(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return mask


def __contourBoxes(contours, imh, imw, radius):

    boxes = []
    for c in contours: # find box location
        x, y, w, h = cv2.boundingRect(c)
        box = [x, y, x+w, y+h]
        boxes.append(box)

    expanded_boxes = []
    for box in boxes: # expand boxes
        x1, y1, x2, y2 = box
        nx1, ny1 = x1-radius, y1-radius
        nx2, ny2 = x2+radius, y2+radius
        expanded_boxes.append([max(0,nx1), max(0,ny1), min(imw, nx2), min(imh, ny2)])

    return expanded_boxes


def __rotatedContourBox(contour):
    
    tl, wh, theta = cv2.minAreaRect(contour)
    box = cv2.boxPoints((tl, wh, theta))
    box = [np.int32(box)]

    return box, tl, wh, theta


def __contoursFromMask(mask):

    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def __filterContoursBySize(contours, min_size, max_size, thin_aspect=0.5):

    filtered_contours = []
    for c in contours:
        if cv2.contourArea(c) < min_size:
            continue # small contours
        c = cv2.convexHull(c)
        if cv2.contourArea(c) > max_size:
            continue # large contours
        rect = cv2.minAreaRect(c)
        w, h = rect[1]
        if max(w,h) * thin_aspect > min(w,h):
            continue # thin contours
        filtered_contours.append(c)
    
    return filtered_contours



"""Public functions for use in scripts"""



def annotateImage(img, contours, filtered_contours, contour_boxes, 
    contour_color=[0,200,200], filtered_contour_color=[0,100,255], box_color=[0,0,200]):

    annotated_img = img.copy()
    cv2.drawContours(annotated_img, contours, -1, color=contour_color, thickness=2)
    cv2.drawContours(annotated_img, filtered_contours, -1, color=filtered_contour_color, thickness=2)
    for box in contour_boxes:
        cv2.rectangle(annotated_img, (box[0], box[1]), (box[2], box[3]), color=box_color, thickness=2)

    return annotated_img

def annotateLabel(label, label_box, 
    norm_sensitivity=230, box_color=[0,200,0]):

    # Find background
    gray = cv2.cvtColor(label, cv2.COLOR_BGR2GRAY)
    bg = cv2.dilate(gray, np.ones((11,11), np.uint8), iterations=2)
    bg = cv2.medianBlur(bg, 21)

    # Remove background and normalize
    diff = 255-cv2.absdiff(gray, bg)
    norm = diff.copy()
    cv2.normalize(diff, norm, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    ret, thr = cv2.threshold(norm, norm_sensitivity, 0, cv2.THRESH_TRUNC)
    cv2.normalize(thr, thr, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    thr = cv2.merge([thr, thr, thr]) # make threshold three channels

    # Create mask to insert annotated label
    binary_label = np.zeros_like(label)
    cv2.fillPoly(binary_label, label_box, [255,255,255])
    binary_label = binary_label>0 # convert to logical

    # annotate the label
    annotated_label = label.copy()
    annotated_label[binary_label] = thr[binary_label]
    cv2.drawContours(annotated_label, label_box, -1, color=box_color, thickness=2)
    
    return annotated_label

def findLabelsApprox(img, dilate_iterations, sensitivity, min_label_size, max_label_size, radius):

    # inits
    h, w = img.shape[:2]

    # create mask
    gray = __dilateEqualizeGray(img, dilate_iterations)
    mask = __threshMask(gray, sensitivity)

    # find label positions
    contours = __contoursFromMask(mask)
    filtered_contours = __filterContoursBySize(contours, min_label_size, max_label_size)
    label_locations = __contourBoxes(filtered_contours, h, w, radius)

    annotated_img = annotateImage(img, contours, filtered_contours, label_locations)

    return annotated_img, label_locations


def findLabelExact(label, label_location, sensitivity, min_label_size, max_label_size):

    # create mask
    mask = __autoMask(label)

    # find exact label positions
    contours = __contoursFromMask(mask)
    filtered_contours = __filterContoursBySize(contours, min_label_size, max_label_size)
    label_box, tl, wh, theta = __rotatedContourBox(filtered_contours[0]) # use largest contour

    annotated_label = annotateLabel(label, label_box, sensitivity)
    x = label_location[0] + tl[0]
    y = label_location[1] + tl[1]
    exact_pos = [x,y]
    w, h = wh
    perimeter = 2*(w+h)
    area = w*h

    return annotated_label, exact_pos, theta, perimeter, area

