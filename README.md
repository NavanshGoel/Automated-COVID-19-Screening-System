# Automated-COVID-19-Screening-System

## Abstract 
In order to prevent the spread of COVID-19, ensuring universal mask usage in public places, using sanitiser and prevention of contact with infected people is an essential task. Manually checking the above can become tedious and also increase chances of spread of infection for working personnel. We propose that a smart sanitiser dispenser which checks the temperature would help decrease the spread of the disease. Further, we would like to implement a camera that ensures that the person entering the establishment is wearing a mask. The device will check the temperature of the person while dispensing the sanitiser. Further, the camera checks the person’s face and detects whether the person is wearing a mask or not. If the person is wearing a mask the system rotates the barrier and allows the person to move inside the premises. This device can be placed in college entrances and the entry of the students and professors can be allowed on proper fulfilment of the mentioned conditions. We plan on using Raspberry Pi along with some object detection techniques to solve the proposed solution. The decision to use Raspberry Pi is due to the availability of both object detection libraries like OpenCV and versatile microcontroller properties.


## Introduction
The aim of this project is to enable automatic contactless, speedy screening for COVID-19.While speed is important, this is a soft real time task as failure to achieve the deadline only causes discomfort and does not crash the system. Raspberry pi is a microcontroller board with high computational capabilities.It has an ARM/Broadcom SoC (System on Chip) with a GPU, RAM and both wireless and wired connectivity options. It is a flexible platform that powers developers to create a wide range of applications. With the need to support object detection models and some sensors, Raspberrypi was the ideal choice of controller for this project. The sensors used for this project are:
- LM35 Temperature sensor to measure the temperature of a person
- PIR sensor to detect the presence of a hand
- PiCam module to detect mask
- Sanititser pump
- Motor to rotate barrier 

This project was implemented as a simulation using Proteus software. Proteus offers a great range for the peripherals that can be added. The addition of peripherals allows integration of a variety of modules and functionalities.
