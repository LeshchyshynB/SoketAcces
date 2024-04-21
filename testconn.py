# import socket


# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("212.115.110.10", 7546))
# print("YES")
# client.close()
# import time
# exec 195.160.206.155 import pyautogui; pyautogui.mouseDown(button='left'); time.sleep(1); pyautogui.mouseUp(button='left')
# exec 195.160.206.155 import pyautogui; pyautogui.keyDown('w'); time.sleep(1); pyautogui.keyUp('w')
# exec 195.160.206.155 import pyautogui; pyautogui.typewrite('SvinoreZZ')

# import os
# for i in range(10): os.system("start")
#exec 195.160.206.155 import pyautogui; pyautogui.mouseDown(button='left'); time.sleep(0.1); pyautogui.mouseUp(button='left')
# import time

# exec("import pyautogui; [pyautogui.mouseDown(button='left'), time.sleep(0.1), pyautogui.mouseUp(button='left')] * 7")

from datetime import datetime, timezone
value = "21.04.2024/14.36.00"
date1 = datetime.strptime(datetime.now(timezone.utc).strftime("%d.%m.%Y/%H.%M.%S"), f"%d.%m.%Y/%H.%M.%S")
date2 = datetime.strptime(value, f"%d.%m.%Y/%H.%M.%S")
print(date1 - date2)
print()