# Color-Sorter
This project integrates a Raspberry Pi (Logic & UI) and an Arduino (Sensor Control) to build a fully automated sorting machine. It uses a custom GPIO Pulse Protocol to synchronize hardware events with a multi-threaded Python interface, allowing for real-time tracking, sorting, and manual overrides.

DISCLAIMERS: YOU MUST BE ON RASPBERRY PI TO HAVE ACCESS TO THE RPi.GPIO library. Otherwise, the python code will not run. AFAIK, RPi.GPIO is not available on laptop. For color_identify.ino color sensor logic and inputs must be calibrated to your own color sensor. Factors like ambient light, type of sensor, size of object you want to scan, etc will make the code for my color sensor different from the code you must use for accurate results. color_identify.ino code should be pasted onto the Arduino IDE and uploaded to an Arduino Nano. color_sorter_python.py should be uploaded to a python IDE on the raspberry pi. The IDE i used was Thonny. 

Video demonstrations and a circuit schematic can be found below. You may refer to the second video below to see the actual circuitry but for an **actual readable schematic**, please refer to the image at the **bottom of the page**

# **YOUTUBE VIDEO COLOR SORTER DEMO**
[![Color Sorter Demo](https://private-user-images.githubusercontent.com/232115392/537077886-0fc8af2e-87a8-40ff-a1a8-666c2bdce8f7.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njg2MjE4MDgsIm5iZiI6MTc2ODYyMTUwOCwicGF0aCI6Ii8yMzIxMTUzOTIvNTM3MDc3ODg2LTBmYzhhZjJlLTg3YTgtNDBmZi1hMWE4LTY2NmMyYmRjZThmNy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDExN1QwMzQ1MDhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04Mzg4MDA5NTk3NTI4ODU0Mjg5NGVhYjJiNDAwYTY1ZTUzZDdjZTAzODQxNmQ0ZGI5ZmYyMzFmMzA4ZTU4MDRlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.AlBK2s5jPcBPjp-_HM8kz0hTqwiuy43u0TG0FnzUSko)](https://www.youtube.com/watch?v=9fzAuMDgA8s)

# **Video Showing Circuitry**
[![Color Sorter Circuitry](https://private-user-images.githubusercontent.com/232115392/537078008-8f840425-83ec-4f5c-b66f-0ad2392fa737.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njg2MjE3NjQsIm5iZiI6MTc2ODYyMTQ2NCwicGF0aCI6Ii8yMzIxMTUzOTIvNTM3MDc4MDA4LThmODQwNDI1LTgzZWMtNGY1Yy1iNjZmLTBhZDIzOTJmYTczNy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDExN1QwMzQ0MjRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00ZWFiYjllNmRlYjNkZGQxNDU2MjZjYzczZmIxNTk0NTVlN2YxMWI4ZTRlNGJjMWViZDU5YWUwOTYwNTlkMzkzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.QQM91jlJC37jSreb_f7m9k0kgbB_5o7ozhrTLSGBC3o)](https://www.youtube.com/watch?v=T-Vl8kB1nAQ)

# **Circuit Schematic**
<img width="2816" height="1504" alt="Circuit Schematic" src="https://github.com/user-attachments/assets/0217b41c-1932-4696-8eaf-e7c4cb77777d" />

