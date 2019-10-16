# Heart-Pulse Monitoring System using Raspberry Pi 3 with Real-time streaming and visualization.

Heart-Pulse Monitoring System using Raspberry Pi 3 with Real-time streaming and visualization.


Introduction:  We have made a simple heart-pulse monitoring system with the help of pulse sensors and combining raspberry pi 3 with it. Then we used a web platform (InitialState) to visually represent the data in real time.

Equipment: 
Hardware:
1.	Raspberry Pi 3
2.	Pulse-Sensor
3.	Jumper Wires
4.	Ethernet Cable (for initial Setup)
5.	Analog to Digital converter
Software apps & Online Services:
1.	Raspbian OS
2.	Disk Imager
3.	Pycharm
4.	Initial State’s API

How it works:  
1.	First we have to setup the Raspberry Pi 3 along with the pulse sensor.
2.	Then we have to run our Heartbeat.py script from the raspberry pi to start recording pulse.
3.	Then we have to put our hands on the pulse sensor to give input.
4.	Step 3 will show the pulse in the terminal of the raspberry pi.
5.	When it is running, the heart beat data will be uploaded in Initial state website’s interface. For this, first we had to create a data stream bucket which gave us a bucket key and access key to connect our code to the website’s API.
6.	In the Initial state’s interface we can see our heart-pulse data visually represented nicely.


Future possibilities & Modification:   This project may be built with less cost in the future with modifications like, faster data upload and streaming with improved accuracy.

Motive:  This can be utilized to make remote patient’s data accessible to doctors outside the area.


Sensor Code Credit : http://udayankumar.com/2016/05/17/heart-beat-raspberry/

Streamer Code - Self
