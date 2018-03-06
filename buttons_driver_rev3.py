'''
@filename: buttons_driver_rev3.py
@author: james_rolfe
@updated: 20180306
@about: This contains the buttons driver code for the rev3 board
'''

from gpiozero import Button

# translate pin numbers to GPIO numbers as per documentation:
# https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering
# if a pin is not listed, then it cannot be used as a GPIO pin
PIN_MAP = {3:   2,
	   5:   3,
	   7:   4,
	   8:  14,
    	   10: 15,
    	   11: 17,
    	   12: 18,
    	   13: 27,
    	   15: 22,
    	   16: 23,
    	   18: 24,
    	   19: 10,
    	   21:  9,
    	   22: 25,
    	   23: 11,
    	   24:  8,
    	   26:  7,
    	   29:  5,
    	   31:  6,
    	   32: 12,
    	   33: 13,
    	   35: 19,
    	   36: 16,
    	   37: 26,
    	   38: 20,
    	   40: 21}

class Button_struct():
	'''
	@params:
		pin: 
                    (int) the number of the pin on the board (not GPIO number)
		name: 
                    (str) the name of the button
		action_pressed: 
                    (func) the function to perform when the button is presssed
                action_released:
                    (func) the function to perform when the button is released,
                    defaults to None
	@ret:
		button_struct object. To use gpiozero button calls, use self.button
	@about:
		Call this function to create a new gpiozero button with meta-data.
	'''
	def __init__(self, pin, name, action_pressed, action_released=None):
        	self.name = name
		self.pin = pin
                self.button = None
		
		# init gpiozero Button 
		try:
		    self.button = Button(PIN_MAP[pin])
                    
                    # this has to point to the function, not what the function
                    # returns thus use "lambda:" when passing the function 
                    self.button.when_pressed = action_pressed
                    self.button.when_released = action_released
		except KeyError:
                    print "ERROR: Bad pin number for " + name + " button\n"

# testing
def button_test(name):
    print "Button \"" + name + "\" press detected!"

if __name__ == '__main__':
        home      = Button_struct(3, "home", lambda: button_test("home"))
	vol_min   = Button_struct(5, "vol_min", lambda: button_test("vol_min"))
	vol_add   = Button_struct(7, "vol_add", lambda: button_test("vol_add"))
	display   = Button_struct(8, "display", lambda: button_test("display"))
	mute      = Button_struct(10, "mute", lambda: button_test("mute"))
	start     = Button_struct(11, "start", lambda: button_test("start"))
	select    = Button_struct(12, "select", lambda: button_test("select"))
        green_r   = Button_struct(13, "green_right", lambda: button_test("green_right"))
        red_r     = Button_struct(15, "red_right", lambda: button_test("red_right"))
 	blue_r    = Button_struct(16, "blue_right", lambda: button_test("blue_right"))
	yellow_r  = Button_struct(18, "yellow_right", lambda: button_test("yellow_right"))
	trigger_r = Button_struct(22, "trigger_right", lambda: button_test("trigger_right"))
	trigger_l = Button_struct(29, "trigger_left", lambda: button_test("trigger_left"))
	green_l   = Button_struct(31, "green_left", lambda: button_test("green_left"))
	bumper_r  = Button_struct(32, "bumper_right", lambda: button_test("bumper_right"))
	red_l     = Button_struct(33, "red_left", lambda: button_test("red_left"))
	blue_l    = Button_struct(35, "blue_left", lambda: button_test("blue_left"))
	bumper_l  = Button_struct(36, "bumper_left", lambda: button_test("bumper_left"))
	yellow_l  = Button_struct(37, "yellow_left", lambda: button_test("yellow_left"))

	while(True):
		foo = 0










