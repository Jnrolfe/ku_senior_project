import spidev
import time
import os
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[0]&3) << 8) + adc[1]
  return data
 
# Define sensor channels
# (channels 3 to 7 unused)
x_channel = 0
y_channel = 1
 
# Define delay between readings (s)
delay = 0.5
 
while True:
 
  # Read the joystick position data
  x_pos = ReadChannel(x_channel)
  y_pos = ReadChannel(y_channel)
 
  # Print out results
  print "--------------------------------------------"
  print("X : {}  Y : {} ".format(y_pos,x_pos))
 
  # Wait before repeating loop
  time.sleep(delay)
