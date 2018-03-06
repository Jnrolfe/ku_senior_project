from __future__ import division
import spidev
import time
import os
import uinput
from gpiozero import Button, MCP3002

device = uinput.Device([
    uinput.BTN_LEFT,
    uinput.BTN_RIGHT,
    #uinput.REL_X,
    #uinput.REL_Y,
    uinput.KEY_ENTER,
    uinput.KEY_DOWN,
    uinput.KEY_UP,
    uinput.KEY_SPACE,
    uinput.KEY_LEFT,
    uinput.KEY_RIGHT,
    uinput.KEY_W,
    uinput.KEY_S,
    uinput.KEY_A,
    uinput.KEY_D
    ])


def response2():
    device.emit(uinput.BTN_LEFT, 1)
def response2_2():
    device.emit(uinput.BTN_LEFT, 0)
def response3():
    device.emit_click(uinput.KEY_ENTER, 1)
def response4():
    device.emit_click(uinput.KEY_SPACE, 1)
def response5():
    device.emit_click(uinput.BTN_RIGHT, 1)

left = Button(22)
left.when_pressed = response2
left.when_released = response2_2
up = Button(23)
up.when_pressed = response3
down = Button(27)
down.when_pressed = response4
right = Button(24)
right.when_pressed = response5
    
def bitstring(n):
    s = bin(n)[2:]
    return '0'*(8-len(s)) + s

def read(adc_channel, spi_channel):
    conn = spidev.SpiDev(0, spi_channel)
    conn.max_speed_hz = 1200000 # 1.2 MHz
    conn.mode = 1
    cmd = 192
    if adc_channel:
        cmd += 32 #32
    reply_bytes = conn.xfer2([cmd, 0])
    #print reply_bytes
    reply_bitstring = ''.join(bitstring(n) for n in reply_bytes)
    reply = reply_bitstring[5:15]
    conn.close()
    return int(reply, 2) / 2**10

def main():
    
    while True:
        #Initialize joystick values
        #joystick_x_left = 0
        joystick_y_left = 0
        #joystick_x_right = 0
        #joystick_y_right = 0
          
        #Average out every thirty values
        #for i in range(0,30):
        #      joystick_x_left += int(read(1,1)*1000)
        #      joystick_y_left += int(read(0,1)*1000)
        #      joystick_x_right += int(read(1,0)*1000)
        #      joystick_y_right += int(read(0,0)*1000)


	joystick_x_left = int(read(1,0)*1000)
	joystick_y_left = int(read(0,0)*1000)
	#print(joystick_x_left)
	#print(joystick_y_left)
	#print('-')
		
        
        #joystick_x_left = joystick_x_left/30
        #joystick_y_left = joystick_y_left/30
        #joystick_x_right = joystick_x_right/30
        #joystick_y_right = joystick_y_right/30

        
        if joystick_x_left >= 525:
	    device.emit(uinput.KEY_D, 0)
	    device.emit(uinput.KEY_A, 1)
	    device.emit_click(uinput.KEY_LEFT, 1)
        #    device.emit(uinput.REL_X, 10)
        elif ((joystick_x_left <= 325) and (joystick_x_left > 75)):
	    device.emit(uinput.KEY_A, 0)
	    device.emit(uinput.KEY_D, 1)
	    device.emit_click(uinput.KEY_RIGHT, 1)
	#    device.emit(uinput.REL_X, -10)
        else:
	    device.emit(uinput.KEY_A, 0)
	    device.emit(uinput.KEY_D, 0)

        if joystick_y_left >= 525:
	    device.emit(uinput.KEY_S, 0)
	    device.emit(uinput.KEY_W, 1)
	    device.emit_click(uinput.KEY_UP, 1)
        #    device.emit(uinput.REL_Y, 10)
        elif ((joystick_y_left <= 325) and(joystick_y_left > 75)):
	    device.emit(uinput.KEY_W, 0)
	    device.emit(uinput.KEY_S, 1)
	    device.emit_click(uinput.KEY_DOWN, 1)
        #    device.emit(uinput.REL_Y, -10)
	else:
	    device.emit(uinput.KEY_S, 0)
	    device.emit(uinput.KEY_W, 0)

        time.sleep(.1) #.01
                    
if __name__ == "__main__":
   main()
