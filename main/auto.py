import numpy as np
import pandas as pd
import os
from exec import get_data

# Parameters (change as desired)
    # Root chord: 6 - 15
    # Tip chord: 3 - 10
    # Height: 3 - 4
    # Angle: 30 - 70
#  Check to make sure valid simuations are run in OpenRocket using the most extreme geometry combination

sus_root_chord_list = np.arange(6, 7, 0.5)     # Including 15
sus_tip_chord_list = np.arange(3, 3.5, 0.5)      # Including 10
sus_height_span_list = np.arange(3, 3.1, 0.1)     # Including 4
sus_angle_list = np.arange(68, 70, 2)             # Including 70

data = []
count = 0
for sus_root_chord in sus_root_chord_list:
    for sus_tip_chord in sus_root_chord_list:
        for sus_height_span in sus_height_span_list:
            for sus_angle in sus_angle_list:
                print(f"Root chord: {sus_root_chord} in")
                print(f"Tip chord: {sus_tip_chord} in")
                print(f"Height/Span: {sus_height_span} in")
                print(f"Angle: {sus_angle} deg")
                
                relevant_data = get_data(sus_root_chord, sus_tip_chord, sus_height_span, sus_angle)

                row = {
                    "Root Chord (in)": relevant_data[0],
                    "Tip Chord (in)": relevant_data[1],
                    "Height/Span (in)": relevant_data[2],
                    "Sweep Length (in)": relevant_data[3],
                    "Angle (deg)": relevant_data[4],
                    "Base stability (%)": relevant_data[5],
                    "Max stability (%)": relevant_data[6],
                    "Time of max stability": relevant_data[7],
                    "CNAlpha @ Max Mach": relevant_data[8],
                    "Min damping ratio": relevant_data[9],
                    "Max damping ratio": relevant_data[10],
                    "Altitude (ft)": relevant_data[11]
                }

                # Append the row to the data list
                data.append(row)
                count = count + 1

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data/auto output data.csv", index=False)
