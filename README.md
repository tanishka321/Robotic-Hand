# Robotic-Hand
Robotic Hand mimics the user's finger gestures through Raspberry Pi camera module.

![Robotic_hand](https://user-images.githubusercontent.com/123478223/215149512-2b479927-b4da-41a5-96b4-c5bb2ca6ac70.jpeg)

Using OpenCV library in Python critical points on the hand are detected and ratio of the distance between the joints of the fingers seen by the camera are sent to the Microcontroller. Ratio of distance has been taken into consideration rather than just taking distance as the distance between camera and hand varies which results in the variation of distance between joint of hand.

# Hardware 
1. Microcontroller board (Raspberrypi zero 2W)
2. Servo motors
3. Raspberry pi camera module

![apparatus](https://user-images.githubusercontent.com/123478223/215149798-4ff2c81d-7ff5-4098-84ae-17b34a66a093.jpeg)

The ratios of the distance of all the fingers is transferred to Raspberry pi and accordingly move the servo motors corresponding to every finger.

![Finger_structure](https://user-images.githubusercontent.com/123478223/215150653-b667fe31-b0ea-411a-8139-0d85bb673812.jpeg)
Structure of finger

# Prerequisites
1. Computer Vision
2. SSH 
3. Basics of Linux



