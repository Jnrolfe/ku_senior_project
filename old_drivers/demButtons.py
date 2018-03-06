from gpiozero import Button


def response1():
    print("We got buttons! Left")
def response2():
    print("We got buttons! Up")
def response3():
    print("We got buttons! Down")
def response4():
    print("We got buttons! Right")
def response5():
    print("We got buttons! rLeft")
def response6():
    print("We got buttons! rUp")
def response7():
    print("We got buttons! rDown")
def response8():
    print("We got buttons! rRight")

left = Button(6)
up = Button(13)
down = Button(19)
right = Button(26)
rleft = Button(22)
rup = Button(23)
rdown = Button(27)
rright = Button(24)

left.when_pressed = response1
up.when_pressed = response2
down.when_pressed = response3
right.when_pressed = response4
rleft.when_pressed = response5
rup.when_pressed = response6
rdown.when_pressed = response7
rright.when_pressed = response8

while True:
        foo = 0
