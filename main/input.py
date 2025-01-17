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

get_data(sus_root_chord, sus_tip_chord, sus_height_span, sus_angle)

## TO DO: Export to a CSV file to organize the outputs