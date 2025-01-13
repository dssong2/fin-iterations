import pyautogui as ag
import time

def setup():
    ag.click(8, 51) # Can optimize by clicking directly to what tab will get to
    ag.press('tab')
    ag.keyDown('up')
    time.sleep(3) # Give sufficient time for it to go to top of the list
    ag.keyUp('up')
    for i in range(30):
        ag.press('up')
    for i in range(13):
        ag.press('down')
    ag.press('tab')
    ag.press('space')

def input_geometry(root_chord, tip_chord, height_span, sweep_length):
    for i in range(4):
        ag.press('tab')
    ag.typewrite(str(root_chord))
    ag.press('tab')
    ag.typewrite(str(tip_chord))
    ag.press('tab')
    ag.typewrite(str(height_span))
    ag.press('tab')
    ag.typewrite(str(sweep_length))
    for i in range(16):
        ag.press('tab')
    ag.press('enter')

# Test input: 13.9, 5, 3, 7.815