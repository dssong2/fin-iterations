import pygetwindow as gw
from pygetwindow import getWindowsWithTitle

def activate_window(window_title):
    # Get all windows with the matching title
    windows = gw.getWindowsWithTitle(window_title)
    
    if windows:
        window = windows[0]  # Assuming there's only one window matching the title
        if window.isMinimized:
            window.restore()  # Restore the window if it's minimized
        window.activate()  # Bring the window to the foreground
        print(f"Window with title '{window_title}' found.")
    else:
        print(f"Window with title '{window_title}' not found.")
        exit()

def minimize_window(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        windows[0].minimize()
        print(f"Minimized window: {window_title}")
    else:
        print(f"Window '{window_title}' not found.")
        exit()
