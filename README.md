# Color-Sorter
This project integrates a Raspberry Pi (Logic & UI) and an Arduino (Sensor Control) to build a fully automated sorting machine. It uses a custom GPIO Pulse Protocol to synchronize hardware events with a multi-threaded Python interface, allowing for real-time tracking, sorting, and manual overrides.

DISCLAIMERS: YOU MUST BE ON RASPBERRY PI TO HAVE ACCESS TO THE RPi.GPIO library. Otherwise, the python code will not run. AFAIK, RPi.GPIO is not available on laptop. For color_identify.ino color sensor logic and inputs must be calibrated to your own color sensor. Factors like ambient light, type of sensor, size of object you want to scan, etc will make the code for my color sensor different from the code you must use for accurate results. color_identify.ino code should be pasted onto the Arduino IDE and uploaded to an Arduino Nano. color_sorter_python.py should be uploaded to a python IDE on the raspberry pi. The IDE i used was Thonny. 

Video demonstrations and a circuit schematic can be found below. You may refer to the second video below to see the actual circuitry but for an **actual readable schematic**, please refer to the image at the **bottom of the page**

# **YOUTUBE VIDEO COLOR SORTER DEMO**
[![Color Sorter Demo](https://private-user-images.githubusercontent.com/232115392/537056282-c3432c69-ce08-4b4a-a713-72b11f98b7ef.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njg2MDczNDgsIm5iZiI6MTc2ODYwNzA0OCwicGF0aCI6Ii8yMzIxMTUzOTIvNTM3MDU2MjgyLWMzNDMyYzY5LWNlMDgtNGI0YS1hNzEzLTcyYjExZjk4YjdlZi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDExNlQyMzQ0MDhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xZWI5ZDgzMDdhZmZjYjQ4MjU3NGUzNWZjN2ZjZTM2NTNjZjE3Njc3ZTgwZjBlOGJjMTg4MTZjZGMzODM5ZWNmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Zxo4wuDL4dSUTL6zzBAfRJuTnJ0FUTkFldU4ulsC398)](https://www.youtube.com/watch?v=9fzAuMDgA8s)

# **Video Showing Circuitry**
[![Color Sorter Circuitry](https://private-user-images.githubusercontent.com/232115392/537056854-b416f3dd-ccac-4a11-96c0-49c937b60dc5.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njg2MDc1OTksIm5iZiI6MTc2ODYwNzI5OSwicGF0aCI6Ii8yMzIxMTUzOTIvNTM3MDU2ODU0LWI0MTZmM2RkLWNjYWMtNGExMS05NmMwLTQ5YzkzN2I2MGRjNS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDExNlQyMzQ4MTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04MmQ5MDMwNTc2ZmM3YWU5YzkxZWY1ZGU5NDc1Njg3NmIzYjQyYzhiMDNkODg1N2M2MDYxYTZlMjE0ZTcyYmQzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Bo8UtgLFBjNOSbSUdXnwTzKQCHojcwVRGfXm8ETnwcA)](https://www.youtube.com/watch?v=T-Vl8kB1nAQ)

# **Circuit Schematic**
<img width="2816" height="1504" alt="Circuit Schematic" src="https://github.com/user-attachments/assets/0217b41c-1932-4696-8eaf-e7c4cb77777d" />

