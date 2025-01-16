import numpy as np
import pygetwindow as gw
import openrocket.or_input as ori
import ras.ras_input as rasi
import openrocket.or_output as oro
import ras.ras_output as raso
from helpers.windows import activate_window, minimize_window

## Identify correct window name
file_name = input("Enter the OpenRocket file name (do not include .ork extension): ")
open_rocket = f"Rocket ({file_name}.ork)"

## Must minimize first before activating
minimize_window(open_rocket)
minimize_window("RASAero II")

## Geometry constants
sus_diameter = 3.12

# Parameters
    # Root chord: 6 - 10
    # Tip chord: 3 - 10
    # Height: 3 - 4
    # Angle: 30 - 70

## TO DO: Create automation of the program with these values in the array
values_root_chord = np.arange(6, 15.5, 0.5)     # Including 15
values_tip_chord = np.arange(3, 10.5, 0.5)      # Including 10
values_height_span = np.arange(3, 4.1, 0.1)     # Including 4
values_angle = np.arange(30, 72, 2)             # Including 70

## TO DO: Adjust input for angle, not sweep length, adjust macro in or_input as well

## Geometry input variables, sweep length input
root_chord = float(input("Root chord (in): ")) ## DATA POINT ##
assert root_chord >= 6.0
tip_chord = float(input("Tip chord (in): ")) ## DATA POINT ##
assert tip_chord >= 3.0
height_span = float(input("Height/Span (in): ")) ## DATA POINT ##
assert height_span >= 3.0
angle = float(input("Angle (deg): ")) ## DATA POINT ##
assert angle <= 70.0, "Angle must be less than 70 degrees"

sweep_length = height_span * np.tan(np.radians(angle))
print(f"Sweep length (in): {sweep_length} in")

## OpenRocket ##
activate_window(open_rocket)
ori.setup()
ori.input_geometry(root_chord, tip_chord, height_span, angle)

oro.component_analysis()

## or_output stuff, return relevant numbers and store them as variables for rasaero use
oro.valid_full_stability()

sus_length = oro.get_length(root_chord, tip_chord, sweep_length) # Stability percent calculations
base_stability = oro.get_stability(sus_length) ## DATA POINT ##
sus_mass = oro.get_mass()[0] # RASAero input
sus_CG = oro.get_CG()[0] # RASAero input

full_mass = oro.get_mass()[1] # RASAero input
full_CG = oro.get_CG()[1] # RASAero input

## Get min/max damping ratio
DR = oro.get_DR()
min_DR = DR[0] ## DATA POINT ##
max_DR = DR[1] ## DATA POINT ##
minimize_window(open_rocket)

## RASAero ##
activate_window("RASAero II")
rasi.setup()
rasi.input_geometry(root_chord, tip_chord, height_span, sweep_length)
rasi.input_or_data(sus_CG, sus_mass, full_CG, full_mass)
raso.get_ras_data()
raso.get_aero_plot()
minimize_window("RASAero II")

values = raso.get_ras_values(sus_length)

altitude = values[0] ## DATA POINT ##
max_stability_percent = values[1] ## DATA POINT ##
max_stability_time = values[2] ## DATA POINT ##
CNalpha = values[3] ## DATA POINT ##

print("Relevant Data: ")

print(f"Base stability: {base_stability}%")
print(f"Max stability percent: {max_stability_percent}%")
print(f"Max stability time: {max_stability_time} s")
print(f"CNalpha value: {CNalpha}")
print(f"Min damping ratio: {min_DR}")
print(f"Max damping ratio: {max_DR}")
print(f"Altitude: {altitude} ft\n")

print("Supporting data: ")
print(f"Sustainer length: {sus_length} in")
print(f"Sustainer mass with motors: {sus_mass} lb")
print(f"Sustainer CG: {sus_CG} in")
print(f"Full stack mass with motors: {full_mass} lb")
print(f"Full stack CG: {full_CG} in")
