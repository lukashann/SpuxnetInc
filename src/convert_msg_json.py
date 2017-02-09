import json
import time

def convert_msg(msg_arr):
    '''Takes an array containing the predicted colour and the RGB.
    Convert these and a timestamp to a dict, that is then converted to
    a json payload.'''
    predicted_colour = msg_arr[0]
    rgb_values = msg_arr[1]
    timestamp = time.ctime()
    colour_dict = {}

    colour_dict['Predicted Colour'] = predicted_colour
    colour_dict['RGB values'] = rgb_values
    colour_dict['Time'] = timestamp

    payload = json.dump(colour_dict)

    return payload
