import pyautogui as ag
import pygetwindow as gw
import time

def setup():
    ag.doubleClick(92, 175)
    ag.press('enter')

def input_geometry(root_chord, tip_chord, height_span, sweep_length):
    for i in range(3):
        ag.press('tab')
    ag.hotkey('ctrl', 'a')
    ag.typewrite(str(root_chord))
    for i in range(3):
        ag.press('tab')
    ag.hotkey('ctrl', 'a')  
    ag.typewrite(str(sweep_length))
    ag.press('tab')
    ag.hotkey('ctrl', 'a')
    ag.typewrite(str(tip_chord))
    ag.press('tab')
    ag.hotkey('ctrl', 'a')
    ag.typewrite(str(height_span))
    for i in range(8):
        ag.hotkey('shift', 'tab')
    ag.press('enter')
    for i in range(4):
        ag.press('tab')
    ag.press('enter')

def input_or_data(sus_CG, sus_mass, full_CG, full_mass):
    ag.click(570, 78) # Clicks on "Flight simulation"
    while True:
        if (gw.getWindowsWithTitle("Flight")):
            ag.doubleClick(280, 152) # Click on the "Motor(s) loaded", enters "FlightDataEntry" window
            break
        time.sleep(0.1)
    while True:
        if (gw.getWindowsWithTitle("FlightDataEntry")):
            time.sleep(0.25) # New pop-up/window opens
            ag.press('tab')
            ag.hotkey('ctrl', 'a')
            ag.typewrite(sus_CG)
            for i in range(2):
                ag.press('tab')
            ag.hotkey('ctrl', 'a')
            ag.typewrite(sus_mass)
            for i in range(4):
                ag.press('tab')
            ag.hotkey('ctrl', 'a')
            ag.typewrite(full_CG)
            for i in range(2):
                ag.press('tab')
            ag.hotkey('ctrl', 'a')
            ag.typewrite(full_mass)
            for i in range(3):
                ag.press('tab')
            for i in range(2):
                ag.press('enter')
            ag.hotkey('shift', 'tab')
            ag.press('space') # Selects "View Data" button, runs simulation
            break
        time.sleep(0.25)