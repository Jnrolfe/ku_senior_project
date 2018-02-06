'''
@filename: buttons_driver_rev3.py
@author: james_rolfe
@updated: 20180205
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
		pin: (int) the number of the pin on the board (not GPIO number)
		name: (str) the name of the button
		action: (func) the function to perform when the button is presssed
	@ret:
		button_struct object. To use gpiozero button calls, use self.button
	@about:
		Call this function to create a new gpiozero button with meta-data.
	'''
	def __init__(self, pin, name, action):
		self.name = name
		self.pin = pin
		
		# init gpiozero Button 
		try:
			self.button = Button(PIN_MAP[pin])
		except KeyError:
			print "Bad pin number for " + name + " button\n"
		
		# TESTING -- replace action in production
		self.button.when_pressed = action(self)

# testing
def button_test(button):
	print "Button \"" + self.name + "\" press detected!"

if __name__ == '__main__':
	home      = Button_struct(3, "home", button_test)
	vol_min   = Button_struct(5, "vol_min", button_test)
	vol_add   = Button_struct(7, "vol_add", button_test)
	display   = Button_struct(8, "display", button_test)
	mute      = Button_struct(10, "mute", button_test)
	start     = Button_struct(11, "start", button_test)
	select    = Button_struct(12, "select", button_test)
	green_r   = Button_struct(13, "green_right", button_test)
	red_r     = Button_struct(15, "red_right", button_test)
	blue_r    = Button_struct(16, "blue_right", button_test)
	yellow_r  = Button_struct(18, "yellow_right", button_test)
	trigger_r = Button_struct(22, "trigger_right", button_test)
	trigger_l = Button_struct(29, "trigger_left", button_test)
	green_l   = Button_struct(31, "green_left", button_test)
	bumper_r  = Button_struct(32, "bumper_right", button_test)
	red_l     = Button_struct(33, "red_left", button_test)
	blue_l    = Button_struct(35, "blue_left", button_test)
	bumper_l  = Button_struct(36, "bumper_left", button_test)
	yellow_l  = Button_struct(37, "yellow_left", button_test)

	while(True):
		foo = 0










