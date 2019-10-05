# bluetooth-refresher
Will automatically access the annoyingly not-easily-accessible Windows 8.1 bluetooth settings, and toggle the bluetooth off and then on again.


The Problem:
  In Windows 8.1, whenever you want to access the bluetooth setting you have to go to: PC settings -> PC and devices -> Bluetooth. As long as you use bluetooth device for more than the PC, any time you want to pair it with the PC again after it was connected to another device you will have to do this navigating and toggling. This will also happen occasionally regardless.
  
The Solution:
  A python script that uses pyautogui package, to do all the navigating and toggling for you. 

Usage:
Initializing:
  1. Download some python interpreter (was tested with 3.6) and install the pyautogui package.
  2. The script and the batch should preferably be placed in \wherever-your-python-folder-is\Python36\Scripts
  3. Edit the batch file and enter the path to the bluetooth-refresher.py file. 
  4. Activate using the bbb.batch script (which was named that way to be easily findable through winKey+s). 
  
The limits of this application:
- Should have python interpreter and the pyautogui package installed.
- Obviously this probably only works in Windows 8.1 (I assume also in 8)
- More Assumptions: the screen is 1920x1080 resolution, bluetooth  should be On, and you should always exit the PC settings with the x button or alt+F4 (otherwise in "PC settings" it will stay on the bluetooth screen and now everything is different). There is probably a solution to all of these but this is good enough for me for now :) 

I might generalize this to be more user friendly later.
