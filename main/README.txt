Safety Information:
    1. This program is essentially a massive macro, which means if a keyboard or mouse command doesn't
       do what it's supposed to do, it will probably execute the remaining commands wildly somewhere else
    2. Please close all other open windows except VSCode, your OpenRocket file, and your RASAero file in
       case of unexpected macros being executed anywhere where they shouldn't be
    3. Make sure the rocket files you have open are what you want to run iterations on
    4. ** If anything doesn't look right (like if your rocket suddenly has 8 fins), drag your mouse to
       any corner of the screen to end this program **
    5. Follow the setup process listed below exactly as follows, skipping a step may result in macro
       anomalies
    6. If you have any problems whatsoever, let me know at a meeting or email me at dssong2

Setup Process:
    OpenRocket (version 24.12.beta.1):
        1. Open the OpenRocket file you would like to run fin iterations on
            a. ** VERY IMPORTANT: YOU MUST FULLSCREEN THE WINDOW ** 
        2. Copy the file name (do not include .ork), you will need this later when prompted
        3. Ensure you have Damping Ratio custom expression setup. If not, follow these steps:
            a. Go to "Tools" at the top of the window
            b. Click "Custom expressions"
            c. Click "New expression"
            d. Fill in the boxes as follows:
                Name: Damping Ratio
                Symbol: DR
                Units: [none, leave blank]
                Expression: Cdm /(2*sqrt( Ccm * Il ))
            e. Click "OK" and then "Close"
        4. Go to "Flight Simulations" tab
        5. Click on the pre-existing simulation, or create new one if none exist
        6. Verify your launch conditions, adjust as needed
        7. Click "OK"
        8. Click "Run simulations"
        9. Click "Plot / Export" and go to "Export data"
        10. Check off only "Time" and "Damping Ratio" in the checklist
        11. Check screenshot to ensure everything is the same (sustainer only, # comment options)
        12. Click on "Export"
        13. Select the export file location to the "openrocket" folder
            a. Relative path: "...\Fin Iteration Automation\main\openrocket"
            b. You can find the path to this folder by typing "pwd" in the terminal
            c. Example path: C:\Users\astro\OneDrive - University of Illinois - Urbana\ISS\SDA 24-25\Fin Iteration Automation\main
            e. This will ensure everytime the code runs, it will always save to the same destination
        14. Name the file "damping ratio", DO NOT CHANGE THIS NAME
            a. We want to overwrite this file through iterations so we don't end up with a million damping ratio files :D
        15. Click "Save", overwrite file if it already exists
        16. Click "Close"
        17. Ensure rocket is show in full stack mode (sustainer and booster)
    
    RASAero:
        1. Open corresponding RASAero file
            a. ** VERY IMPORTANT: YOU MUST FULLSCREEN THE WINDOW **
        2. Make sure you place your RASAero file in the "ras" folder
            a. Path should be .../Fin Iteration Automation/main/ras/
            b. This will ensure all exported data will save in the ras folder and be accessible
        3. Ensure motor files have been imported (check for correct motors in "Flight Simulations)
            a. File > Select motor file
            b. Select rasp.eng
            c. If you don't have rasp.eng downloaded, ask someone on the team
        4. Click on "Flight simulation"
        5. Drag the opened window to the upper left corner (very important!)
        6. Double click on the simulation under "Motor(s) loaded"
        7. Check for correct motors are selected and right nozzle exit diamters
        8. Close the two open windows, return to RASAero main window