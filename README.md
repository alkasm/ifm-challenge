# Intelligent Flying Machines 

I ran this pipeline on the two images provided, and also created two modified images to 
experiment on; a rotated version of the low resolution image, and a flipped version of 
the low resolution image with two additional labels placed onto the box.

The pipeline returns the annotated images: the label is normalized and outlined in green. 

![High res](highres_annotated.jpg) 
![Low res](lowres_annotated.jpg)
![Low res, rotated](lowres_rot_annotated.jpg)
![Low res, modified](lowres_mod_annotated.jpg)

# Scripts and functions

    labelFinder.py -- contains the main functions for finding and annotating labels
    highres_ex_script.py -- a script to input parameters and run the functions in labelFinder.py
    lowres_ex_script.py -- a script to input parameters and run the functions in labelFinder.py
    labelWindow.py -- contains functions for displaying trackbars and updates the window with parameter changes
    parameter_trackbar_ex_script.py -- a script to run labelWindow.py; example images were input here
    
# Requirements

These scripts and functions have been tested on OpenCV 3.2.0, OpenCV 3.1.0, Python 3.5.2, and Python 3.6.1.
