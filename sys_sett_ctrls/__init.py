# A basic module that provides ways of controlling the microphone
#
# Currently available functionalities:
# - Get the name of the microphone
# - Get the current input volume
# - Set the input volume


# system_controls/__init__.py
from .mic_control import MicCtrl

__all__ = ["MicCtrl"]
