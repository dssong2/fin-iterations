import pyautogui as ag
import pandas as pd
import re
import pyperclip as pc
import time
import os

sus_data = None
full_data = None

def component_analysis():
    global sus_data, full_data
    for i in range(2):
        ag.press('alt')
        for a in range(2):
            ag.press('left')
        ag.press('enter')
        ag.press('c') # Opens new pop-up/window
        time.sleep(1)
        if i != 0:
            for b in range(8):
                ag.press('tab')
                time.sleep(0.1)
            ag.press('space')
            time.sleep(1)
        for _ in range(12):
            ag.press('tab')
            time.sleep(0.1)
        ag.hotkey('ctrl', 'c')
        if i == 0:
            full_data = pc.paste()
        else:
            sus_data = pc.paste()
        ag.press('esc')

    # Return to full stack mode
    ag.doubleClick(8, 51) # Click on "Rocket design"
    for d in range(9):
        ag.press('tab')
        time.sleep(0.1)
    ag.press('space')

# ** Must be run before get_stability() **
def get_length(root_chord, tip_chord, sweep_length):
    base_length = 74.85 # inches, adjust as needed
    overhang = tip_chord - root_chord + sweep_length
    if (overhang < 0):
        return base_length
    sus_length = base_length + overhang
    return sus_length

## Solve with CG and CP and sustainer diameter
def get_stability(sus_length):
    data = re.findall(r"\d+\.\d+", sus_data)
    assert data[3] > data[2], "Negative susatiner stability"
    stability_perc = (float(data[3]) - float(data[2])) / sus_length * 100.0
    return stability_perc

def valid_full_stability():
    data = re.findall(r"\d+\.\d+", full_data)
    assert data[3] > data[2], "Negative full-stack stability"

## Get from Tools > Component analysis
def get_mass():
    return [re.findall(r"\d+\.\d+", sus_data)[0], re.findall(r"\d+\.\d+", full_data)[0]]

## Get from Tools > Component analysis
def get_CG():
    return [re.findall(r"\d+\.\d+", sus_data)[2], re.findall(r"\d+\.\d+", full_data)[2]]

## Get damping ratio export data
def get_DR_data():
    ag.click(365, 55) # Clicks on "Flight simulations"
    while True:
        ag.hotkey('ctrl', 'c')
        data = pc.paste()
        if "Up to date" in data:
            ag.hotkey('ctrl', 'e') # Opens new pop-up/window
            time.sleep(1)
            for i in range(2):
                ag.press('tab')
            for i in range(3):
                ag.press('right')
            for i in range(3):
                ag.hotkey('shift', 'tab')
            ag.press('enter') # Opens new pop-up/window
            time.sleep(1.5)
            ag.typewrite('damping ratio')
            for i in range(2):
                ag.press('enter')
            ag.press('esc')
            ag.click(8, 51) # Click on "Rocket design"
            break
        time.sleep(0.5)

def get_DR():
    get_DR_data()
    file_path = os.path.abspath("openrocket/damping ratio.csv")
    data = pd.read_csv(file_path)
    data_filtered = data[(data['# Time (s)'] > 4.0) & (data['Damping Ratio ()'] > 0.0)]
    min_value = data_filtered['Damping Ratio ()'].min()
    max_value = data_filtered['Damping Ratio ()'].max()
    return [min_value, max_value]
