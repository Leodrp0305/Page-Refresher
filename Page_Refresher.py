import pyautogui
import time

#Now we gotta be using the info we got in Pixel_Scanner.py

print("Refresing the page each 5 seconds. CTRL + C to stop.")

try:
    while True:
        pyautogui.press('f5')  # press f5
        time.sleep(5)
        pixel_color = pyautogui.pixel(130,148) #put the coordinates in the parentheses
        if pixel_color != (207, 0, 0): #put the code rgb in the parentheses
            break
except KeyboardInterrupt:
    print("\nStoping the code.") 
    #the code gotta interrupt if the color change or you press CTRL + C