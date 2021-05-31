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

## Engineering design 

### For the design of the model we have designed the following modules:

- Sanitiser Dispenser
- Temperature Check
- Mask Detection
- Automated entry gate



### To simulate the system on Proteus, we have made use of the software simulations of the following hardware components:

- PIR sensor to detect the presence of a hand
- Sanititser pump
- LM35 Temperature sensor to measure the temperature of a person
- PiCam module to detect mask
- Motor to rotate barrier 

### The working of the system happens in the following way:

User places hand below the sanitiser dispenser, which also has a temperature sensor(LM35) to measure the temperature. The presence of a hand is detected by a PIR sensor.
After a hand is detected by the PIR sensor, the sanitiser is dispensed using a pump and the temperature is measured.
If the temperature value is within the allowable range, then the mask detection module will be signalled. If the temperature is not in the allowable range, then a warning message will be displayed showing that the temperature is out of the range.
This signal switches on the PiCam, which then checks for the presence of a mask.
If a mask is detected, the motor of the entry gate will be enabled which will allow the user to enter the premises.
If no mask is detected or mask is worn incorrectly, then a warning message will be displayed showing that mask is not worn.

### About each module:

### Sanitiser Dispenser and Temperature Check Modules

These two modules are linked together using the PIR sensor which detects the presence of a hand. If a hand is detected, then these two modules will be enabled which leads to disposal of sanitiser by the sanitiser pump and measuring of temperature by the LM35 sensor.

The dispenser is implemented using a DC pump to pump the liquid out of the container holding the sanitiser.

The automated temperature checking module is implemented in order to minimize contact and human interaction.

### Mask Detection Module

The mask detection module will be enabled if the user’s temperature is within the threshold limits.
The mask detector module is implemented using a PiCam module and a machine learning model which is trained using a mask detection dataset, which is downloaded from the Internet. The dataset contains various images of people wearing and not wearing masks and people wearing masks but in the wrong manner. Using these images, the model will be trained in order to correctly identify a person wearing a mask in the right manner.
For training the model, we used OpenCV library to convert the live stream into frames, so that the model can perform the testing. 
If the visitor is wearing the mask properly, he/she will be allowed to proceed further.  

### Automated Entry Gate Module

If the visitor satisfies all the conditions that are set by the system, then the entry gate will automatically be opened, which will allow the visitor to enter the campus. This entry gate is implemented using a servo motor which functions based on the signal it receives. If it receives a positive signal, then the gate is opened, else it remains closed.


## Connections:

### Sanitiser pump module:

L293D motor driver- interfaced with raspberry pi 

INV1 - pin18
INV2 - pin 22
VSS,VS ,EN1 - 12v supply 
OUT1,OUT2 - two ends of motor 

Motor - one end to OUT1 and other to OUT2 of motor driver 

### Barrier opening:

L293D motor driver- interfaced with raspberry pi 

INV1 - pin 32
INV2 - pin 33
VSS,VS ,EN1 - 12v supply 
OUT1,OUT2 - two ends of motor 

Motor - one end to OUT1 and other to OUT2 of motor driver 

### Temperature check module:

LM35- interfaced with ADC 

VCC  - 5v
OUT - ADC’s CH0
GND- gnd pin 

ADC MP3208 - interfaced with Raspberry pi

CLK - CLK
DIN - MOSI
DOUT - MISO
CS - CS
VREF - 3.3v
AGND - GND  

### Hand presence check - PIR SENSOR - interfaced with raspberry pi 

OUT - pin 29
Vcc - 5v
GND - gnd
Test pin - High granularity Interactive potentiometer 

LCD - interfaced with raspberry pi 

RW - GND
VDD - GND 
D4 - pin 7
D5- pin 11
D6- pin 12
D7- pin 13
RS - pin 15
E - pin 16 

## Conclusion and Future Work 

After the implementation of our system, we were able to successfully implement what we have planned for in the beginning. This system will be a very useful one in large campuses such as our college. It reduces human effort vastly and also can reduce fights between security guards and the users as systems are very strict and will not allow entry unless all conditions are strictly satisfied. The system is fully working as far as we have implemented it. 

In the future we can improve our project on the following grounds:

Interface the PiCam module as well in the Proteus simulation
Implementation of the actual hardware system can be done after the pandemic 
If we perform the hardware implementation, we can use an ultrasonic sensor instead of PIR sensor to detect the presence of a hand as it would give better results. 
