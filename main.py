# The main system tray application


# Imports
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
from sys_sett_ctrls import MicCtrl



# Microphone control
microphone = MicCtrl()


# Functions for system try menu actions
def show_volume(icon, item):
    vol = microphone.get_input_volume()
    print(f"Current microphone volume: {vol}%")

def set_volume(icon, item):
    microphone.set_input_volume(0.8) # Set volume to 80%
    print("Volume set to 80%")

def quit(icon, item):
    icon.stop()


#Load the icon image
def icon_image():
    return Image.open("assets/mic_settings.png")


# Define the system tray menu
menu = Menu(
    MenuItem('Show volume', show_volume),
    MenuItem('Set volume to 80%', set_volume),
    MenuItem('Quit', quit)
)


# Initialize the tray icon
icon = Icon("Mic Input Volume Control", icon_image(), menu=menu)


# Run the app
if __name__ == '__main__':
    icon.run()