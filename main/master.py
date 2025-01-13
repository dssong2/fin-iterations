import runpy as rp
import pyautogui as ag
import time

import openrocket.or_input as ori
import ras.ras_input as rasi
import openrocket.or_output as oro
from helpers.windows import activate_window, minimize_window

## Identify correct window name
file_name = input("Enter the OpenRocket file name (do not include .ork extension): ")
open_rocket = f"Rocket ({file_name}.ork)"

## Must minimize first before activating
minimize_window(open_rocket)
minimize_window("RASAero II")

## Geometry input variables
length = 74.85 # inches
root_chord = float(input("Root chord (in): "))
tip_chord = float(input("Tip chord (in): "))
height_span = float(input("Height/Span (in): "))
sweep_length = float(input("Sweep length (in): "))

print(f"Root chord (in): {root_chord}")
print(f"Tip chord (in): {tip_chord}")
print(f"Height/Span (in): {height_span}")
print(f"Sweep length (in): {sweep_length}")

## Begin macro to input geometry variables
activate_window(open_rocket)
ori.setup()
ori.input_geometry(root_chord, tip_chord, height_span, sweep_length)
for i in range(11):
    ag.press('tab')
ag.press('space')

## or_output stuff, return relevant numbers and store them as variables for rasaero use
stability = oro.get_stability()
print(stability)

minimize_window(open_rocket)

activate_window("RASAero II")
rasi.setup()
rasi.input_geometry(root_chord, tip_chord, height_span, sweep_length)
for i in range(4):
    ag.press('tab')
ag.press('enter')
## more input stuff from or_output