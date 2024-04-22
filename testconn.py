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

import subprocess
# cmd = [ 'echo', '1' ]
output = subprocess.Popen(["dir"], stdout=subprocess.PIPE, shell=True).communicate()[0]
print(output)