import pyautogui as ag
import time

def setup():
    ag.doubleClick(8, 51) # Click on "Rocket design"
    ag.press('tab')
    for i in range(35):
        ag.press('up')
    for i in range(13):
        ag.press('down')
    ag.press('tab')
    ag.press('space') # Opens new pop-up/window

def input_geometry(root_chord, tip_chord, height_span, angle):
    time.sleep(1)
    for _ in range(4):
        ag.press('tab')
    ag.typewrite(str(root_chord))
    ag.press('tab')
    ag.typewrite(str(tip_chord))
    ag.press('tab')
    ag.typewrite(str(height_span))
    ag.press('tab')
    ag.press('tab')
    ag.typewrite(str(angle))
    ag.press('tab')
    ag.press('esc')

def sustainer_mode():
    ag.doubleClick(8, 51) # Click on "Rocket design"
    for i in range(9):
        ag.press('tab')
        ag.sleep(0.1)
    ag.press('space')

def full_stack():
    for i in range(9):
        ag.press('tab')
    ag.press('space')
# Test input: 13.9, 5, 3, 7.815