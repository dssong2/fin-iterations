import pyautogui as ag
import pandas as pd
import pygetwindow as gw
import time

def get_ras_data():
    while True:
        current_windows = gw.getAllTitles()
        flight_windows = [title for title in current_windows if title == "Flight"]
        # Check if there are exactly two "Flight" windows
        if len(flight_windows) == 2:
            time.sleep(1)
            ag.press('alt')
            for i in range(3):
                ag.press('enter')
            time.sleep(0.5)
            ag.press('tab')
            ag.press('enter')
            time.sleep(0.5)
            ag.press('enter')
            time.sleep(0.5)
            ag.press('y') # Exports file to VSCode here
            break  # Exit the loop once the code has run            
        time.sleep(2)  # Check every 1 second
    for i in range(2): # Close the windows, return to main RASAero window
        time.sleep(0.25)
        ag.hotkey('alt', 'f4')
    time.sleep(0.25)
    ag.press('enter')

def get_aero_plot():
    ag.click(459, 86) # Click on Aero Plots, opens new window
    time.sleep(1)
    while True:
        open_windows = gw.getWindowsWithTitle("Aero Plots")
        if open_windows:  # If the window is open
            time.sleep(0.25)
            ag.press('alt')
            for i in range(4):
                ag.press('enter')
                time.sleep(0.25)
            ag.press('y') # Export file to VSCode
            time.sleep(0.25)
            break
        time.sleep(1)
    ag.hotkey('alt', 'f4')

def get_alt_stab_time_mach(sus_length):
    data = pd.read_csv(r'C:\Users\astro\OneDrive - University of Illinois - Urbana\ISS\SDA 24-25\Fin Iteration Automation\main\ras\Flight Test.CSV')
    altitude = data['Altitude (ft)'].max()
    altitude_idx = data['Altitude (ft)'].idxmax()
    altitude_time = data.loc[altitude_idx, 'Time (sec)']

    data_filtered = data[(data['Time (sec)'] > 4.0) & (data['Time (sec)'] < altitude_time)]

    max_stability = data_filtered['Stability Margin (cal)'].max()
    max_stability_percent = float(max_stability) * 3.12 / float(sus_length) * 100
    max_stability_idx = data_filtered['Stability Margin (cal)'].idxmax()
    max_stability_time = data_filtered.loc[max_stability_idx, 'Time (sec)']

    max_mach = data_filtered['Mach Number'].max()

    return [altitude, max_stability_percent, max_stability_time, max_mach]


def get_ras_values(sus_length):
    values = get_alt_stab_time_mach(sus_length)
    data = pd.read_csv(r'C:\Users\astro\OneDrive - University of Illinois - Urbana\ISS\SDA 24-25\Fin Iteration Automation\main\ras\CD Test.CSV')
    
    max_mach = values[3]
    max_mach = round(max_mach, 2)
    mach_row = data[data['Mach'] == max_mach]
    CNalpha = mach_row['CNalpha (0 to 4 deg) (per rad)'].values[0]
    return [values[0], values[1], values[2], CNalpha]
