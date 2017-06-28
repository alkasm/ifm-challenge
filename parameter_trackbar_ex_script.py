import labelWindow
import cv2
import numpy as np



__author__ = 'Alexander Reynolds'
__email__ = 'ar@reynoldsalexander.com'



# read images, open a window to set parameters and return the annotated images
hires = cv2.imread('data/highres.jpg')
annotated_hires_img, hires_label_locations = labelWindow.display(hires)

# lores = cv2.imread('data/lowres.jpg')
# annotated_lores_img, lores_label_locations = labelWindow.display(lores)

# lores_rot = cv2.imread('data/lowres-rot.jpg')
# annotated_lores_rot_img, lores_rot_label_locations = labelWindow.display(lores_rot)

# lores_mod = cv2.imread('data/lowres-mod.jpg')
# annotated_lores_mod_img, lores_mod_label_locations = labelWindow.display(lores_mod)

# write the results
# cv2.imwrite('highres_annotated.jpg', annotated_hires_img)
# cv2.imwrite('lowres_annotated.jpg', annotated_lores_img)
# cv2.imwrite('lowres_rot_annotated.jpg', annotated_lores_rot_img)
# cv2.imwrite('lowres_mod_annotated.jpg', annotated_lores_mod_img)