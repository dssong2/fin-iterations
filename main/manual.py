import pandas as pd
from exec import get_data

## Geometry input variables, sus_angle input

sus_root_chord = float(input("Root chord (in): ")) ## DATA POINT ##
assert sus_root_chord >= 6.0
sus_tip_chord = float(input("Tip chord (in): ")) ## DATA POINT ##
assert sus_tip_chord >= 3.0
sus_height_span = float(input("Height/Span (in): ")) ## DATA POINT ##
assert sus_height_span >= 3.0
sus_angle = float(input("Angle (deg): ")) ## DATA POINT ##
assert sus_angle <= 70.0, "Angle must be less than 70 degrees"

relevant_data = get_data(sus_root_chord, sus_tip_chord, sus_height_span, sus_angle)
data = []

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

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data/manual output data.csv", index=False)