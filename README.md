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

## Objective:
The main objective of the project is to create an automated screening system that checks for the user’s temperature and mask. The most important aspect of COVID-19 Screening is that the Person does not transmit any kind of germs or virus. Irrespective of these conditions we dispense sanitiser to the person trying to enter the premises. This ensures a sanitary check and also creates awareness amongst people. 

## Motivation:
The increasing COVID cases have had a huge impact on the lives of people. One of the prominent reasons why COVID-19 keeps spreading is that it is invisible to the human eye. The only way to check the presence is using certain indicators like body temperature and possibility of spread. Since these conditions can be checked using the current technologies available to use, this served as a huge motivation for us. Also, this system can be used in laboratories and factories once the COVID-19 virus is diminished. Finding this scalability was another reason for us to continue in this direction.

## Challenges
- The first problem to design and deploy the project was the online mode of communication. Due to the pandemic itself, we could not meet and discuss the plan of action in person.The solution to the above problem was to use a software like proteus. Since it allows addition of peripherals inside the simulation, we could implement the design and workflow without connecting hardware equipment.
- This in turn had another challenge associated with it. The software requires a manual click to change the inputs of the peripherals. The value of the inputs cannot be changed in real time since there will always be a time delay in creating the optimal change in values.
- The mask detection module cannot be implemented on proteus due to camera capture restrictions. Since the camera attached as a peripheral cannot capture, the image detection program doesn’t have any input. The solution to this is simple. The mask detection program is a python file. In the actual hardware implementation, the raspberry pi board would use python files as programs and an actual camera attached to it as a peripheral.
- One of the most tedious tasks was to find documentation related to raspberry pi simulation on proteus. There is very little information online. Even if we found material, it was very specific to the implementation shown in the example.

