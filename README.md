# Fix microphone (input) volume

This is a Windows application that allows easy access to the microphone input volume setting from the taskbar.

If you wish to use this application, go to [Releases](https://github.com/brziga/fix-mic-volume/releases).

## Motivation

> If you want it done right do it yourself.

On Windows (10), the microphone input volume will sometimes change _on its own_. Especially when you're trying to have it less than 100%. And unless you check it, you won't know until someone (who is listening to you) tells you.  
In order to check the volume level and change it, you have to navigate through the settings and it can be a hassle when you have to do it repeatedly. This app aims to simplify that. 

## Roadmap

- [x] Functioning tray application
- [x] Functionality to set the microphone volume
- [x] Standalone executable
- [ ] Current volume displayed
- [ ] Popup message on hover
- [ ] Custom value option for setting the microphone volume
- [ ] Start with Windows
- [ ] Mute and unmute functionality with indication
- [ ] Settings implementation with saving and loading
- [ ] Set and display functionalities for system volume
- [ ] Periodic checks and automatic correction
- [ ] Customization of the menu options
- [ ] Tray icon display the current input volume


## Credits

### Libraries Used

- **pycaw**: A Python library for controlling audio devices.
  - [GitHub Repository](https://github.com/AndreMiras/pycaw)
  
- **pystray**: A library for creating system tray icons.
  - [GitHub Repository](https://github.com/moses-palmer/pystray)
  
- **Pillow**: Python Imaging Library Fork.
  - [GitHub Repository](https://github.com/python-pillow/Pillow)
  
- **comtypes**: A Python COM package.
  - [GitHub Repository](https://github.com/enthought/comtypes)

### Other assets
Icon image by:  
<a href="https://www.flaticon.com/free-icons/voice-recorder" title="voice-recorder icons">Voice-recorder icons created by rukanicon - Flaticon</a>

### License
This project is licensed under the MIT License.
