#
# Automated Color Sorter - Raspberry Pi
# Author: Vincent Zhou
# Interfaces with Arduino via Pulse Protocol to actuate servos and manage the GUI.
#

# Import necessary modules
import tkinter as tk
import tkinter.font
import time
import threading as thread
import RPi.GPIO as GPIO

# Dictionary to track color counts
colors={
    "Purple": 0,
    "Red": 0,
    "Green": 0,
    "Orange": 0,
    "Unknown": 0
}

# Set GPIO pins for servos
scan_servo=24
sort_servo=12

# Global flag to track scanning status
global scanning
scanning=False
print(scanning)

# Initialize main Tkinter window
root=tk.Tk()
root.title("Vincent's Color Sorter Project")
root.geometry("700x400")
root.configure(bg="lavender")

# Setup GPIO
GPIO.setmode(GPIO.BCM)       
GPIO.setup(21,GPIO.IN)
GPIO.setup(scan_servo,GPIO.OUT)
GPIO.setup(sort_servo,GPIO.OUT)

# Setup PWM for servos
sort_servo_obj=GPIO.PWM(sort_servo,50)
scan_servo_obj=GPIO.PWM(scan_servo,50)

# Count variable for sensor readings
count=0
global can_press
can_press=False
global ui_needs_update
ui_needs_update=False
# Create GUI layout
out_frame=tk.Frame(root,bg="lightblue")
out_frame.pack(fill="both",expand=True)
frame=tk.Frame(out_frame,bg="lightblue")
frame.place(relx=0.5,rely=0.5,anchor="center")

global another_now
another_now=float('inf')  # placeholder time
global colorDetected
colorDetected=""

# Function called when Scan Color button is clicked
def clickedScan():
    global can_press 
    if not can_press:
        return
    scanButton.config(text="Scanning...")
    global scanning
    scanning=True 
    global another_now
    another_now=time.time()

# Function to move servo and sort detected color
def moveTo(arg):
    global can_press #checks if can press based on start/pause buttons
    if not can_press:
        return #if can’t press,return function
    try:
        color=arg.cget("text") 
    except Exception:  
        color=arg #allows for both button and text input
    print(color)
#condition statement based on the color 
    if color=="Red": 
        colors["Red"] += 1
        scan_servo_obj.start(9.5) #servo position so there is no hole under skittle
        sort_servo_obj.ChangeDutyCycle(11.2) #specific position to sort red skittle into red box.
    elif color=="Green":
        colors["Green"] += 1
        scan_servo_obj.start(9.5)
        sort_servo_obj.ChangeDutyCycle(10)#specific position to sort red skittle into green box.
    elif color=="Orange":
        colors["Orange"] += 1
        scan_servo_obj.start(9.5)
        sort_servo_obj.ChangeDutyCycle(8.6)#specific position to sort red skittle into orange box.
    elif color=="Purple":
        colors["Purple"] += 1
        scan_servo_obj.start(9.5)
        sort_servo_obj.ChangeDutyCycle(6)#specific position to sort red skittle into purple box.
    elif color=="Unknown":
        colors["Unknown"] += 1   
        scan_servo_obj.start(9.5)
        sort_servo_obj.ChangeDutyCycle(7.6)#specific position to sort red skittle into unknown box.
    
    # Move arm to drop location,wait,reset position
    time.sleep(2)
    scan_servo_obj.ChangeDutyCycle(4.2) #turn servo so there is nothing holding up the skittle so it falls into the ramp
    time.sleep(2) #wait
    scan_servo_obj.ChangeDutyCycle(9.5) #reset the stepper motor controlling the cardboard under the color sensor to ensure it is ready for the next skittle
    sort_servo_obj.stop()
    time.sleep(2)
    scan_servo_obj.stop() 
    time.sleep(2)
    updateCount()

# Reset the color counts
def resetClicked():
    for a in colors.keys():
        colors[a]=0 #set all values in dictionary to 0
    updateCount()

# Start button logic
def startCommand():
    global can_press
    can_press=True #set global can press to true so you can pres button
    startButton.config(text="Started") #change text of buttons
    pauseButton.config(text="Pause")

# Pause button logic
def pauseCommand():
    global can_press
    can_press=False #set can press to false so cant press button since paused
    startButton.config(text="Start") #config texts of buttons
    pauseButton.config(text="Paused")


# GUI Buttons
scanButton=tk.Button(frame,text="Scan Color",command=clickedScan)
resetButton=tk.Button(frame,text="Reset",command=resetClicked)
startButton=tk.Button(frame,text="Start",command=startCommand)
pauseButton=tk.Button(frame,text="Pause",command=pauseCommand)
exitButton=tk.Button(frame,text="Exit",command=lambda: root.destroy())

# Button layout
titleFont=tkinter.font.Font(family="Arial",size=15)
titleLabel=tk.Label(frame,text="Vincent's Color Sorter",anchor=tk.CENTER,font=titleFont)
titleLabel.grid(row=0,column=0,columnspan=5)
resetButton.grid(row=2,column=2,sticky="E")
scanButton.grid(row=2,column=3,sticky="W")
startButton.grid(row=2,column=4,sticky="W")
pauseButton.grid(row=2,column=0,sticky="E")
exitButton.grid(row=2,column=1)

# Update the color count display
def updateCount():
    # Clear previous count display
    for widget in frame.grid_slaves():
        info=widget.grid_info()
        if info['row']==3 or info['row']==4:
            widget.destroy()
    i=0
    for color,count in colors.items():
        if color=="Unknown":
            continue #unknown doesnt have a color property so just do at end
        label=tk.Label(frame,text=f"{color}:{count}",fg=color.lower())
        button=tk.Button(frame,text=color,bg=color.lower())
        button.config(command=lambda currentButton=button: moveTo(currentButton))
        label.grid(row=3,column=i) #place gui widgets on frame
        button.grid(row=4,column=i,sticky="nsew")
        i += 1
    # Display Unknown color
    label=tk.Label(frame,text=f"Unknown:{colors['Unknown']}",fg="black")
    label.grid(row=3,column=i)
    button=tk.Button(frame,text="Unknown",bg="black",fg="white")
    button.config(command=lambda currentButton=button: moveTo(currentButton))
    button.grid(row=4,column=i)

# Background thread to handle GPIO input and color detection
def otherLoop():
    global scanning,ui_needs_update,colorDetected # Ensure these are accessible
    pulse_count=0
    last_pulse_time=0 
    while True:
        # check if pin 21 goes HIGH (signal received)
        if GPIO.input(21)==GPIO.HIGH:
            pulse_count += 1
            last_pulse_time=time.time()
            #debounce
            while GPIO.input(21)==GPIO.HIGH:
                time.sleep(0.01)
        
        # If we have pulses,and it has been more then 0.5 seconds since the last one,the message is complete.
        if pulse_count>0 and (time.time()-last_pulse_time>0.6):
            print(f"Pulses Received: {pulse_count}")
            if scanning:
                found_color=None           
                if pulse_count==2:
                    found_color="Orange"
                elif pulse_count==3:
                    found_color="Purple"
                elif pulse_count==4:
                    found_color="Red"
                elif pulse_count==5:
                    found_color="Green"
                else:
                    found_color="Unknown" 
                if found_color:
                    colorDetected=found_color
                    print(f"Identified: {found_color}")
                    # Signal the main loop to update the UI since tkinter is not thread safe therefore we need to do in main loop
                    ui_needs_update=True 
            # Reset count
            pulse_count=0
        time.sleep(0.01) 

def check_updates():
    global ui_needs_update,scanning,another_now,colorDetected
    if ui_needs_update:
        moveTo(colorDetected)
        updateCount()       # Update the labels safely
        ui_needs_update=False # reset var
        # Stop scanning 
        scanning=False
        scanButton.config(text="Scan Color")

    # 2. Check for Timeout and if so, reset 
    if time.time()-another_now>4 and scanning:
         scanButton.config(text="Scan Color")
         scanning=False
    root.after(100,check_updates)

# Start background thread
t=thread.Thread(target=otherLoop)
t.daemon=True
t.start()

# Start Tkinter main loop
updateCount()
check_updates()
root.mainloop()
