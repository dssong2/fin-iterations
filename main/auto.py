import numpy as np
from exec import get_data

# Parameters
    # Root chord: 6 - 15
    # Tip chord: 3 - 10
    # Height: 3 - 4
    # Angle: 30 - 70

## TO DO: Create automation of the program with these values in the array
sus_root_chord_list = np.arange(6, 15.5, 0.5)     # Including 15
sus_tip_chord_list = np.arange(3, 10.5, 0.5)      # Including 10
sus_height_span_list = np.arange(3, 4.1, 0.1)     # Including 4
sus_angle_list = np.arange(30, 72, 2)             # Including 70

for sus_root_chord in sus_root_chord_list:
    for sus_tip_chord in sus_root_chord_list:
        for sus_height_span in sus_height_span_list:
            for sus_angle in sus_angle_list:
                print(f"Root chord: {sus_root_chord} in")
                print(f"Tip chord: {sus_tip_chord} in")
                print(f"Height/Span: {sus_height_span} in")
                print(f"Angle: {sus_angle} deg")
                get_data(sus_root_chord, sus_tip_chord, sus_height_span, sus_angle)

## TO DO: Export to a CSV file to organize the outputs