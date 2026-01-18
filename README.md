# Color-Sorter
This project integrates a Raspberry Pi (Logic & UI) and an Arduino (Sensor Control) to build a fully automated sorting machine. It uses a custom GPIO Pulse Protocol to synchronize hardware events with a multi-threaded Python interface, allowing for real-time tracking, sorting, and manual overrides.

DISCLAIMERS: YOU MUST BE ON RASPBERRY PI TO HAVE ACCESS TO THE RPi.GPIO library. Otherwise, the python code will not run. AFAIK, RPi.GPIO is not available on laptop. For color_identify.ino color sensor logic and inputs must be calibrated to your own color sensor. Factors like ambient light, type of sensor, size of object you want to scan, etc will make the code for my color sensor different from the code you must use for accurate results. color_identify.ino code should be pasted onto the Arduino IDE and uploaded to an Arduino Nano. color_sorter_python.py should be uploaded to a python IDE on the raspberry pi. The IDE i used was Thonny. 

Video demonstrations and a circuit schematic can be found below. You may refer to the second video below to see the actual circuitry but for an **actual readable schematic**, please refer to the image at the **bottom of the page**

# **YOUTUBE VIDEO COLOR SORTER DEMO**
[![Color Sorter Demo](https://github.com/user-attachments/assets/0fc8af2e-87a8-40ff-a1a8-666c2bdce8f7)](https://www.youtube.com/watch?v=9fzAuMDgA8s)

# **Video Showing Circuitry**
[![Color Sorter Circuitry](https://github.com/user-attachments/assets/8f840425-83ec-4f5c-b66f-0ad2392fa737)](https://www.youtube.com/watch?v=T-Vl8kB1nAQ)

# **Circuit Schematic**
<img width="2816" height="1504" alt="Circuit Schematic" src="https://github.com/user-attachments/assets/0217b41c-1932-4696-8eaf-e7c4cb77777d" />

