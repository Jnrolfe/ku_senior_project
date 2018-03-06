'''
@filename: joysticks_driver_rev3.py
@author: james_rolfe
@updated: 20180306
@about: This contains the joysticks driver code for the rev3 board
'''

# use the following link for build:
# https://www.raspberrypi-spy.co.uk/2014/04/using-a-joystick-on-the-raspberry-pi-using-an-mcp3008/
# use the following link if the kernel has been updated or if an error saying
# spi.open() file cannot be found --> may need to re-enable spi on the pi:
# https://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/

import spidev
import time
import os

class Joystick_struct():
    '''
    @params:
        name: (str) the name of the joystick
        x_chan: (int) the channel to read the x values
        y_chan: (int) the channel to read the y values
        s_chan: (int) the channel to read the button press
        max_speed: (int) max read speed in hertz for the spi device
    @ret:
        joystick_struct object. 
    @about:
        Call this function to create a new joystick with meta-data.
    '''
    def __init__(self, name, x_chan, y_chan, s_chan, max_speed=1000000):
        self.name = name
        self.chan_dict = {"x_chan": x_chan,
                          "y_chan": y_chan,
                          "s_chan": s_chan}
        
        self.spi = spidev.SpiDev()
        self.spi.open(0,0)
        self.spi.max_speed_hz = max_speed
    
    def read_channel(self, chan_name):
        try:
            adc = self.spi.xfer2([1,(8+self.chan_dict[chan_name])<<4,0])
            data = ((adc[1]&3) << 8) + adc[2]
            if chan_name == "y_chan":
                return -norm_pos(data, 5, 1014)
            return norm_pos(data, 15, 1018)
        except(KeyError):
            print "ERROR: Incorrect channel name passed to " + self.name
            print "bad channel name: " + chan_name

    def check_reading_bound(self, pos_val):
        if pos_val > 100:
            # print "WARNING: " + self.name + " upper bound violation!"
            return 100
        elif pos_val < -100:
            # print "WARNING: " + self.name + " lower bound violation!"
            return -100
        else:
            return pos_val
    
def norm_pos(cur_val, min_val, max_val):
    '''
        returns the value normalized between -100 and 100
    '''
    return (2 * float(cur_val - min_val)/(max_val - min_val) - 1) * 100

# testing
if __name__ == '__main__':

    joystick_r = Joystick_struct("right_joystick", 0, 1, 2)
    
    # Define delay between readings (s)
    delay = 0.25
    
    while True:

        # Read the joystick position data
        vrx_pos = joystick_r.read_channel("x_chan")
        vry_pos = joystick_r.read_channel("y_chan")
        
        # Read switch state
        # swt_val = joystick_r.read_channel("s_chan")

        # Print out results
        print "-----------------------------------------"  
        print("X : {}  Y : {}".format(vrx_pos,vry_pos))

        # Wait before repeating loop
        time.sleep(delay)
