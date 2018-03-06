import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

Home = {'pin_num': 3, 'curr_value': 0, 'orig_value': 0}
Vol_min = {'pin_num': 5, 'curr_value': 0, 'orig_value': 0}
Vol_plu = {'pin_num': 7, 'curr_value': 0, 'orig_value': 0}
Disp = {'pin_num': 8, 'curr_value': 0, 'orig_value': 0}
Mute = {'pin_num': 10, 'curr_value': 0, 'orig_value': 0}
Start = {'pin_num': 11, 'curr_value': 0, 'orig_value': 0}
Select = {'pin_num': 12, 'curr_value': 0, 'orig_value': 0}
X = {'pin_num': 13, 'curr_value': 0, 'orig_value': 0}
Sq = {'pin_num': 15, 'curr_value': 0, 'orig_value': 0}
Tr = {'pin_num': 16, 'curr_value': 0, 'orig_value': 0}
Cir = {'pin_num': 18, 'curr_value': 0, 'orig_value': 0}
RT = {'pin_num': 22, 'curr_value': 0, 'orig_value': 0}
LT = {'pin_num': 29, 'curr_value': 0, 'orig_value': 0}
Left = {'pin_num': 31, 'curr_value': 0, 'orig_value': 0}
Up = {'pin_num': 33, 'curr_value': 0, 'orig_value': 0}
Down = {'pin_num': 35, 'curr_value': 0, 'orig_value': 0}
Right = {'pin_num': 37, 'curr_value': 0, 'orig_value': 0}

buttonList = [Home, Vol_min, Vol_plu, Disp, Mute, Start, Select, X, Sq, Tr, Cir, RT, LT, Left, Up, Down, Right]

for i in range(len(buttonList)):
        GPIO.setup(buttonList[i]['pin_num'],GPIO.IN)

prev_input = 0

while True:
        for i in range(len(buttonList)):
                buttonList[i]['curr_value'] = GPIO.input(buttonList[i]['pin_num'])
                if ((not buttonList[i]['orig_value']) and buttonList[i]['curr_value']):
                        print("Press")
                buttonList[i]['orig_value'] = buttonList[i]['curr_value']
        time.sleep(0.05)
