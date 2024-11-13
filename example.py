"""
A simple example of how to use the Via Lighting API
"""
import time

from via_lighting_api import ViaLightingAPI

"""
DEVICE_PID can be None if vendor id
can uniquely identify the keyboard you want to control
"""
DEVICE_VID = 17498
DEVICE_PID = None

try:
    api = ViaLightingAPI(DEVICE_VID, DEVICE_PID)

    api.set_brightness(127)
    time.sleep(1)

    api.set_effect(5)
    time.sleep(1)

    api.set_effect_speed(255)
    time.sleep(1)

    api.set_color([255, 0, 0])
    time.sleep(1)

    api.set_color([170, 255])
    time.sleep(1)

    api.set_color_abs([127, 127, 0])
    time.sleep(1)

    api.save()
    time.sleep(1)

    """
    Warning: 
    _send() is not recommended.
    It will send the command directly to your device, which may cause unexpected result.
    Make sure you fully understand the meaning of the command before sending it.
    For the following example, the command set light effect to 15, "Rainbow Moving Chevron".
    """
    api._send([7, 3, 2, 15])
except Exception as e:
    print(e)
