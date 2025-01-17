import numpy as np
import os

import openrocket.or_input as ori
import ras.ras_input as rasi
import openrocket.or_output as oro
import ras.ras_output as raso
from helpers.windows import activate_window, minimize_window

def get_data(sus_root_chord, sus_tip_chord, sus_height_span, sus_angle):
    folder_path = "./openrocket"
    files = os.listdir(folder_path) # Gets all file names in openrocket folder

    file_name = None
    # Find the OpenRocket file
    for file in files:
        if file.endswith(".ork"):
            file_name = file
            break
    open_rocket = f"Rocket ({file_name})"

    ## Must minimize first before activating
    minimize_window(open_rocket)
    minimize_window("RASAero II")

    sweep_length = sus_height_span * np.tan(np.radians(sus_angle))
    print(f"Sweep length (in): {sweep_length} in")

    ## OpenRocket ##
    activate_window(open_rocket)
    ori.setup()
    ori.input_geometry(sus_root_chord, sus_tip_chord, sus_height_span, sus_angle)

    oro.component_analysis()

    ## or_output stuff, return relevant numbers and store them as variables for rasaero use
    oro.valid_full_stability()

    sus_length = oro.get_length(sus_root_chord, sus_tip_chord, sweep_length) # Adjust base length in oro file as needed
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
    rasi.input_geometry(sus_root_chord, sus_tip_chord, sus_height_span, sweep_length)
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
    print(f"Full stack CG: {full_CG} in\n\n")
