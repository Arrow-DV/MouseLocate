# Made By Arrow-Dev | Ali Hany
# visit us | https://arrow-dev.rf.gd
# Made in 2/27/2024 | Last Update 2/27/2024

# Import Needed Library's
import tkinter as tk
import pyautogui as pyauto
import pyperclip
import keyboard
import json
from tkinter import font
import time

# List To Check Colors
colors = [
    "white",
    "black",
    "red",
    "green",
    "blue",
    "cyan",
    "magenta",
    "yellow",
    "orange",
    "purple",
    "brown",
    "pink",
    "gray",
    "lightgray",
    "darkgray"
]

# Extract Settings
try:
    with open("settings.json", "r") as file:
        settings = json.load(file)
        if settings["activate_fg"] not in colors:
            settings["activate_fg"] = 'lime'
        else:
            activate_fg = settings['activate_fg']
except (FileNotFoundError, json.decoder.JSONDecodeError, KeyError):
    # If the file doesn't exist, create default settings
    settings = {"activate_fg": "lime", "shortcut": "numlock"}
    with open("settings.json", "w") as file:
        json.dump(settings, file)

# Function Copy The Current Position
def copy():
    pyperclip.copy(f"{pyauto.position()[0]},{pyauto.position()[1]}")
    try:
        label.config(fg=activate_fg)
    except:
        label.config(fg="lime")
    time.sleep(1)
    label.config(fg="black")

# Gui
root = tk.Tk()
root.geometry("300x100")
root.attributes("-topmost", True)
root.resizable(False, False)
root.title("Mlocate")
root.focus_set()

# Function Update The Position
def update(label):
    position = pyauto.position()
    label.config(text=f"X : {position[0]}\nY : {position[1]}")
    root.after(1, lambda: update(label))

# Label
font_style = font.Font(root, size=25)
label = tk.Label(text="", font=font_style)
label.pack()

# Register a global hotkey (Num Lock) to call the copy function
try:
    keyboard.add_hotkey(settings["shortcut"], copy)
except:
    try:
        settings['shortcut'] = 'numlock'
        with open("settings.json", "w") as file:
            json.dump(settings, file)
    except:
        pass
    keyboard.add_hotkey("numlock", copy)

# Run The App
update(label)
root.mainloop()
