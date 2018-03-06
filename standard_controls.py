'''
@filename: standard_controls.py
@author: james_rolfe
@updated: 20180306
@about: This script sets the standard controls as the following upon startup:
    right_joystick : mouse
    right_joystick_press :
    left_joystick : WSAD
    left_joystick_press :
    left_four_buttons : G->mouse_left_click, B->, Y->, R-> 
    right_four_buttons : G->, B->, Y->, R->
    right_bumper :
    right_trigger :
    left_bumper :
    left_trigger :
    home :
    select :
'''

# our libraries
import joysticks_driver_rev3 as joysticks
import buttons_driver_rev3 as buttons

# other libraries
import uinput
import time
from math import ceil

## setup device via uinput
# define possible keyboard/mouse key presses
events = (
        uinput.REL_X,
        uinput.REL_Y,
        uinput.BTN_LEFT,
        uinput.BTN_RIGHT,
        )
# load device with events
device = uinput.Device(events)
# define functions of pressing to pass to buttons
l_click_press = lambda: device.emit(uinput.BTN_LEFT, 1)
l_click_release = lambda: device.emit(uinput.BTN_LEFT, 0)

## create buttons
# home      = buttons.Button_struct(3, "home", button_test)
# vol_min   = buttons.Button_struct(5, "vol_min", button_test)
# vol_add   = buttons.Button_struct(7, "vol_add", button_test)
# display   = buttons.Button_struct(8, "display", button_test)
# mute      = buttons.Button_struct(10, "mute", button_test)
# start     = buttons.Button_struct(11, "start", button_test)
# select    = buttons.Button_struct(12, "select", button_test)
green_r   = buttons.Button_struct(13, "green_right", l_click_press, l_click_release)
# red_r     = buttons.Button_struct(15, "red_right", button_test)
# blue_r    = buttons.Button_struct(16, "blue_right", button_test)
# yellow_r  = buttons.Button_struct(18, "yellow_right", button_test)
# trigger_r = buttons.Button_struct(22, "trigger_right", button_test)
# trigger_l = buttons.Button_struct(29, "trigger_left", button_test)
# green_l   = buttons.Button_struct(31, "green_left", button_test)
# bumper_r  = buttons.Button_struct(32, "bumper_right", button_test)
# red_l     = buttons.Button_struct(33, "red_left", button_test)
# blue_l    = buttons.Button_struct(35, "blue_left", button_test)
# bumper_l  = buttons.Button_struct(36, "bumper_left", button_test)
# yellow_l  = buttons.Button_struct(37, "yellow_left", button_test)

## create joysticks
joystick_r = joysticks.Joystick_struct("right_joystick", 0, 1, 2)

# Define delay between readings (seconds)
delay = 0.025

def get_movement(pos_val):
    if pos_val < 0:
        rm = pos_val % -10
    else:
        rm = pos_val % 10
    
    # get value that is divisible by 10
    mo = pos_val - rm

    # return integer between 0 and 10
    return int(mo/10)

def fix_scale(val, factor):
    if val < 0:
        val = (-1) * ceil((-1) * val * factor)
    else:
        val = ceil(val * factor)
    return val

def fix_corners(xmo, ymo):
    diff = abs(abs(xmo) - abs(ymo))
    
    if diff < 2:
        xmo = fix_scale(xmo, 0.70)
        ymo = fix_scale(ymo, 0.70)
    elif diff < 3:
        xmo = fix_scale(xmo, 0.75)
        ymo = fix_scale(ymo, 0.75)
    elif diff < 4:
        xmo = fix_scale(xmo, 0.79)
        ymo = fix_scale(ymo, 0.79)
    
    return int(xmo), int(ymo)

while True:

    # Read the joystick position data
    vrx_pos = joystick_r.read_channel("x_chan")
    vry_pos = joystick_r.read_channel("y_chan")

    # Check/fix readings
    vrx_pos = joystick_r.check_reading_bound(vrx_pos)
    vry_pos = joystick_r.check_reading_bound(vry_pos)

    xmo, ymo = fix_corners(get_movement(vrx_pos), get_movement(vry_pos))

    device.emit(uinput.REL_X, xmo)
    device.emit(uinput.REL_Y, ymo)

    # TESTING: Print out results
    print "--------------------------------------------"  
    print("x_pos : {}  y_pos : {}".format(vrx_pos, vry_pos))
    print("xmo : {}  ymo : {}".format(xmo, ymo))

    # Wait before repeating loop
    time.sleep(delay)
