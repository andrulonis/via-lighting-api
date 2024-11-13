import hid
import colorsys

"""
Global constants
"""
VIA_INTERFACE_NUM = 1
RAW_HID_BUFFER_SIZE = 32

"""
VIA commands
"""
CUSTOM_SET_VALUE = 7
CUSTOM_SAVE = 9

"""
VIA channels
"""
CHANNEL_RGB_MATRIX = 3

"""
VIA rgb matrix entries
"""
RGB_MATRIX_VALUE_BRIGHTNESS = 1
RGB_MATRIX_VALUE_EFFECT = 2
RGB_MATRIX_VALUE_EFFECT_SPEED = 3
RGB_MATRIX_VALUE_COLOR = 4


class ViaLightingAPI:
    device_path = None

    def __init__(self, vid, pid):
        self.device_path = self.find_device(vid, pid)
        if self.device_path is None:
            raise self.DeviceNotFoundError(f"Device not found or does not support VIA.")

    @staticmethod
    def find_device(vendor_id, product_id):
        for device_dict in hid.enumerate():
            if device_dict['vendor_id'] == vendor_id:
                if product_id is None or device_dict['product_id'] == product_id:
                    if device_dict['interface_number'] == VIA_INTERFACE_NUM:
                        return device_dict['path']
        return None

    # def

    @staticmethod
    def rgb_to_hsv(r, g, b):
        r_normalized = r / 255.0
        g_normalized = g / 255.0
        b_normalized = b / 255.0
        h, s, v = colorsys.rgb_to_hsv(r_normalized, g_normalized, b_normalized)
        return h, s, v

    class DeviceNotFoundError(Exception):
        pass
