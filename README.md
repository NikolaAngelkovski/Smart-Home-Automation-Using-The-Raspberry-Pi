# Smart Home Automation Using The Raspberry Pi
**Student Name: Nikola Angelkovski**\
**Student ID: 20095550**
# Introduction
This is a small project made by me for the "IoT Standards & Protocols" course from the Waterford Institute of Technology in Waterford, Ireland. The goal of the project is to make the Raspberry Pi the central hub for controlling IoT devices in the home, such as smart doors, smart fridges etc. The Raspberry Pi can be accessed from a smartphone/tablet/laptop/PC. See the detailed information about the project below.
# Tools, Technologies and Equipment
For this project I was using the following tools, technologies and equipment:
- A Raspberry Pi 4 model B (2GB RAM)
- A Sense HAT add-on board for the Raspberry Pi, which can be used for getting various data such as temperature, humidity, barometric pressure etc. and also getting audiovisual feedback through the built-in 8x8 RGB LED matrix and connected speakers
- Packet Tracer by Cisco, a cross-platform visual simulation tool that allows users to create network topologies and imitate modern computer networks. This was used for simulating IoT devices in a home network, and was controlled by an external app through the Raspberry Pi
- Blynk- A smartphone application that was used for controlling the devices in the Packet Tracer simulation
- ThingSpeak- ThingSpeak is an open-source Internet of Things application and API to store and retrieve data from things using the HTTP and MQTT protocol over the Internet or via a Local Area Network. ThingSpeak was used to create a channel which was used as a monitor for the temperature, humidity and pressure of the simulation. The data was also used to automate the heating/cooling elements, and trigger notifications via IFTTT
- IFTTT- A cloud-based service that allows a user to program a response to events in the world of various kinds. IFTTT will analyze the data from the ThingSpeak channel and if a certain trigger event happens, for ex. the room temperature is above/below the given threshold, then IFTTT will send a mail/text alert message to the user
- An Android smartphone to showcase the Blynk application and its use in the real world
- A laptop/PC to run the simulations for the project and write the necessary Python code for the devices in Packet Tracer
- Visual Studio Code- used for connecting to the RPi via SSH and writing the necessary Python code
# Visual representation of the project
The two pictures below explain how the project should work once everything is set up. The first picture is a roadmap for the development of the project, and the second picture is a diagram which shows visually how the components are going to be connected in the end, with detailed explanation of how the information flows through the components.
![alt text](https://github.com/NikolaAngelkovski/Smart-Home-Automation-Using-The-Raspberry-Pi/blob/main/Development%20roadmap.png) 
<hr style="border:2px solid gray"> </hr>

![alt text](https://github.com/NikolaAngelkovski/Smart-Home-Automation-Using-The-Raspberry-Pi/blob/main/Project%20overview%20diagram.png)
 
# Tutorials and Files
I have created a [playlist](https://www.youtube.com/playlist?list=PLknVyGBYudWuT1P1lZ_0AwqsM6FiRtyYy) that has a couple of tutorials for the project. I also made a folder where you can find all the necessary files.
