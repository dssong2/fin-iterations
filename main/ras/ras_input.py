import pyautogui as ag

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
