"""
@filename: make_binding.py
@author: james_rolfe
@updated: 20180310
@about: This file will create key bindings for the StreamyGamer device
"""

import json
from sys import exit

"""
Button Binding Possibilities:
    Letters:
        Any letter should be entered in the following format:
            '<capital_letter>'
        Where <capital_letter> is any of the following:
            Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M
    Numbers:
        Any number should be entered in the following format:
            '<number>'
        Where <number> is any of the following:
            1,2,3,4,5,6,7,8,9,0
    Function Keys:
        Any function key should be entered in the following format:
            'F<number>'
        Where <number> is any of the following:
            1,2,3,4,5,6,7,8,9,10,11,12
    Misc Keys:
        These keys don't fall into any of the above categories and therefore
        are defined below:
            Escape = 'esc'
            Tilda = 'tilda'
            Tab = 'tab'
            Caps Lock = 'caps'
            Shift = 'shift'
            Control = 'ctrl'
            Windows Key = 'win'
            Alt = 'alt'
            Space Bar = 'space'
            Enter = 'enter'
            Backslash = 'backslash'
            Backspace = 'backspace'
            Minus = 'minus'
            Equals = 'equals'
            Arrow-Left = 'arrow_left'
            Arrow-Right = 'arrow_right'
            Arrow-Up = 'arrow_up'
            Arrow-Down = 'arrow_down'

Joystick Binding Possibilities:
    'WSAD':
        This binding makes the joystick output the following:
            WA      W     WD
                    _
            A      |_|     D

            SA      S     SD
    'SWAD':
        This binding makes the joystick output the following:
            SA      S     SD
                    _
            A      |_|     D

            WA      W     WD
    'mouse':
        This binding makes the joystick control the mouse pointer
    'arrows':
        This binding makes the joystick output the following:
            <up><left>      <up>         <up><right>
                              _
            <left>           |_|             <right>

            <down><left>    <down>     <down><right>
    'arrows_inverted':
        This binding makes the joystick output the following:
            <down><left>    <down>     <down><right>
                              _
            <left>           |_|             <right>

            <up><left>      <up>         <up><right>

Use:
    Use this script to generate a custom key binding. You must provide a unique
    name for your binding by defining the CONFIG_NAME variable.

    See the guides above to know what strings map to which keys. 
"""

config = {}

# example bindings
config['left'] = {
    'joystick': 'mouse',
    'joystick_click': 'ctrl',
    'down': '1',
    'right': '2',
    'up': '3',
    'left': '4'
}
config['right'] = {
    'joystick': 'WSAD',
    'joystick_click': 'shift',
    'down': 'mouse_left_click',
    'right': 'Q',
    'up': 'mouse_right_click',
    'left': 'T'
}
config['middle'] = {
    'left': 'esc',
    'middle': 'tab',
    'right': 'right'
}

# ONLY CHANGE THIS VARIABLE NAME
CONFIG_NAME = 'test_buttons_1'

# test unique-ness
if CONFIG_NAME == 'standard_buttons':
    print "ERROR: Choose a different CONFIG_NAME"
    exit(1)
# force text file format
fout = CONFIG_NAME + '.txt'

# write binding file
with open(fout, 'w') as f:
    json.dump(config, f)


