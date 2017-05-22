# Intelligent Flying Machines 
We make humans as efficient as robots.

At the core, IFM is a Data Analytics Company using Machine Learning,
Computer Vision, and Robotics to automate indoor data capture. We develop
autonomous systems that know where they are and what they see using no
external infrastructure.

[![Intelligent Flying Machines](https://img.youtube.com/vi/AMDiR61f86Y/0.jpg)](https://www.youtube.com/watch?v=AMDiR61f86Y)

## working/flying with IFM
If you are interested in working and flying with IFM, please send us your code for the following challenge:

## the challenge
In some applications, our robots need to find labels on boxes. While there are really awesome machine learning approaches for this, we want you to implement a label detector pipeline using conventional CV methods in C++ (i.e. filters, thresholds, edge detectors, etc.). 

### The inputs to your program are: 
an image with labels either from file or from a ROS topic

As you can see, the two images we give you as a reference are very different. One is very blurry and low resolution, while the other one looks neat and has a higher resolution. We want your code to work with both. 

![Image 1](https://github.com/ifm-tech/cv_coding_challenge/raw/master/data/216.jpg)
![Image 2](https://github.com/ifm-tech/cv_coding_challenge/raw/master/data/506.jpg)

### The outputs of your program should be: 
the position (u,v), orientation (\theta), perimeter (p), area (A), and confidence (\mu) of label detections, published on a ROS topic with a custom ROS message

Throughout our interview process, we will build upon this initial code to see how well you handle building complete vision pipelines, so make sure to keep everything organized. Since you will try to make this pipeline work with other datasets, it is very advisable to implement all tuning parameters as dynamic reconfigure options so you can change them on the fly (no pun intended) with rqt. 

### Here's a few things we like: 
GPUs
very few parameters
robustness to lighting and rotation

## submission
To submit, please fork the repo and email us at jobs@ifm-tech.com

## what we look for
We look for elegantly written, maintainable, and reusable code. We want you to leverage test-driven principles that quantify your implementation's performance. 

And... 

<img src="https://img.devrant.io/devrant/rant/r_109448_5NyDp.jpg" >  
