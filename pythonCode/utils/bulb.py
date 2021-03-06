from tkinter import *
import signal
import sys

def signal_handler(sig, frame):
    print("Ctrl-C pressed")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

root = Tk()

# Add Title & set the Geomtry
root.title('IOT Lamp')
root.geometry("500x700")

# Define Our Images
on = PhotoImage(file = "images/bulb_on.png")
off = PhotoImage(file = "images/bulb_off.png")

def bulbOff():
    bulb.config(image = off)
    my_label.config(text = "The Lamp is Off", fg = "grey")

def bulbOn():
    bulb.config(image = on)
    my_label.config(text = "The Lamp is On", fg = "green")

# Create Label & Bulb
my_label = Label(root,
    text = "The Lamp Is Off!",
    fg = "grey",
    font = ("Helvetica", 32))
my_label.pack(pady = 20)
bulb = Label(root, image = off)
bulb.pack()

def wm_close():
    sys.exit(0)

root.protocol("WM_DELETE_WINDOW", wm_close)

if __name__ == "__main__":
    import time
    is_on = False
    def toggle():
        global is_on
        if is_on:
            is_on = False
            bulbOff()
        else:
            is_on = True
            bulbOn()
        root.after(2000, toggle)
    root.after(2000, toggle)
    root.mainloop()
else:
    def mainloop():
        root.mainloop()    
    def after(t, f):
        root.after(t, f)    
    def update():
        root.update()    

