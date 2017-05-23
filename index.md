# Intelligent Flying Machines 
We make humans as efficient as robots.

At the core, IFM is a Data Analytics Company using Machine Learning,
Computer Vision, and Robotics to automate indoor data capture. We develop
autonomous systems that know where they are and what they see using no
external infrastructure.

[![Intelligent Flying Machines](https://img.youtube.com/vi/AMDiR61f86Y/0.jpg)](https://www.youtube.com/watch?v=AMDiR61f86Y)

## flying with IFM
We are currently hiring Computer Vision Software Engineers to join our team full time in Chicago. A big part of our hiring process is designed around working through and implementing a vision pipeline from scratch. You will start with the basics and as you progress through the different stages in our interview process, you and your software will grow. If you make it all the way through to the very end, we will fly you in for a day, work hands on with you to implement the last parts and finally test and run your code on our robots in a real warehouse. 

## the challenge, stage 1
In some applications, our robots need to find labels on boxes. While there are really awesome machine learning approaches for this, we want you to implement a label detector pipeline using conventional CV methods in C++ (i.e. filters, thresholds, edge detectors, etc.). You can use OpenCV 3.2 if you want, but if you decide to implement some of the vision primitives from scratch, that's excellent! 

### the inputs to your program are: 
an image either from a file or from a ROS topic (2 provided)

As you can see, the two images we give you as a reference are very different. One is very blurry and low resolution, while the other one looks neat and is high resolution. We want your code to work with both. 

![Image 1](https://github.com/ifm-tech/cv_coding_challenge/raw/master/data/216.jpg)
![Image 2](https://github.com/ifm-tech/cv_coding_challenge/raw/master/data/506.jpg)

### the outputs of your program should be: 
the position (u,v), orientation (theta), perimeter (p), area (A), and confidence (mu) of label detections, published on a ROS topic with a custom ROS message

Throughout our interview process, we will build upon this initial code to see how well you handle building complete vision pipelines, so make sure to keep everything organized. Since you will try to make this pipeline work with other datasets, it is very advisable to implement all tuning parameters that you need as dynamic reconfigure options so you can change them on the fly (literally) with rqt. 

### here's a few things we like: 
1) GPUs
2) very few parameters
3) robustness to lighting and rotation

## submission
To submit, please fork the repo and email us at jobs@ifm-tech.com

## what we look for
We look for elegantly written, maintainable, and reusable code. We want you to leverage test-driven principles that quantify your implementation's performance. 

And... 

<img src="https://img.devrant.io/devrant/rant/r_109448_5NyDp.jpg" >  
