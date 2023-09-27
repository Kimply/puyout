import pyautogui
import time

while True:
    x, y = pyautogui.position()
    print(f" x={x}, y={y}")
    time.sleep(.1)  # منتظر یک ثانیه بمانید تا موقعیت موس به‌روز شود

