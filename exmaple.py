from via_lighting_api import ViaLightingAPI

"""
DEVICE_PID can be None if vendor id
can uniquely identify the keyboard you want to control
"""
DEVICE_VID = 17498
DEVICE_PID = None

try:
    api = ViaLightingAPI(DEVICE_VID, DEVICE_PID)
except Exception as e:
    print("Error initializing API:", e)