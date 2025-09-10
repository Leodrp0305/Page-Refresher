import pyautogui # type "pip install pyautogui" in the cmd if pyauto is showing some error.
import time

print ("Put your mouse over the pixel you want the coordinates")
time.sleep(3) # 3 seconds to put yout mouse over the desired pixel.

x, y = pyautogui.position()
pixel_color = pyautogui.pixel(x, y)
print(f"The pixel's coordinate is: ({x}, {y})")
print (f"Cor do pixel em ({x},{y}): {pixel_color}")
