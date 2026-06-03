import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# 1. Map your pin connections
keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3,) 
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 2. Define the Cut, Copy, and Paste macros for Windows
# LCTRL means "Left Control"
keyboard.keymap = [
    [
        KC.LCTRL(KC.X),  # Key 1: Cut (Ctrl + X)
        KC.LCTRL(KC.C),  # Key 2: Copy (Ctrl + C)
        KC.LCTRL(KC.V),  # Key 3: Paste (Ctrl + V)
    ],
]

if __name__ == '__main__':
    keyboard.go()