# Microphone controls class and methods


# Imports
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL



class MicCtrl:
    # Class that provides methods to control the microphone

    def __init__(self, microphone=None):
        # Constructor
        self.device = self._get_microphone()
        if not self.device:raise Exception("No microphone found!")

        self.interface = self.device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume_control = self.interface.QueryInterface(IAudioEndpointVolume)

    def _get_microphone(self):
        # Find and return the default microphone device
        return AudioUtilities.GetMicrophone()
    
    def microphone_name(self):
        # Get the name of the microphone (meant for display)
        return self.device.friendlyName
    
    def get_input_volume(self):
        # Get the current input volume
        current_volume = self.volume_control.GetMasterVolumeLevelScalar()
        return round(current_volume * 100, 2)
    
    def set_input_volume(self, volume):
        # Set the input volume
        if not (0.0 <= volume <= 1.0): raise ValueError("Volume must be between 0.0 and 1.0")

        self.volume_control.SetMasterVolumeLevelScalar(volume, None)