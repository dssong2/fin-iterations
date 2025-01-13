from PIL import ImageGrab
from pytesseract import image_to_string
import pyautogui as ag

## Get screenshot of "Mass with motors" from OpenRocket (to use in RasAero)
def get_stability():
    screen_width, screen_height = ag.size()
    print(f"Screen resolution: {screen_width}x{screen_height}")
    x1, y1 = 2312, 690
    x2, y2 = 2532, 710
    graph_region = (x1, y1, x2, y2)  # Adjust based on your screen
    stability = ImageGrab.grab(bbox=graph_region)

    # Step 5: Extract data using OCR
    output_text = image_to_string(stability)
    stability.save("stability.png")
    return output_text
## Get screenshot of CG and image_to_string it (to use in RasAero)
## Store the stability percentage (to return, needed data)
## Click on "Booster" again to get full stack CG and "Mass with motors"
## Screenshot CG and "Mass with motors"

## Damping ratio stuff