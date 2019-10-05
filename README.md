# bluetooth-refresher
Will automatically access the annoyingly not-easily-accessible Windows 8.1 bluetooth settings, and toggle the bluetooth off and then on again.


The Problem:
  In Windows 8.1, whenever you want to access the bluetooth setting you have to go to: PC settings -> PC and devices -> Bluetooth. As long as you use bluetooth device for more than the PC, any time you want to pair it with the PC again after it was connected to another device you will have to do this navigating and toggling.
  
The Solution:
  A python script that uses pyautogui package, to do all the navigating and toggling for you. 

Usage:
  1. Initializing: Edit the batch file and enter the path to the bluetooth-refresher.py file. 
  2. Activate using the bbb.batch script (which was named that way to be easily findable through winKey+s). 
  
The limits of this application:
- Should have python interpreter and the pyautogui package installed.
- The script and the batch should preferably be placed in \wherever-your-python-folder-is\Python36\Scripts
- Obviously this probably only works in Windows 8.1 (I assume also in 8)
- More Assumptions: the screen is 1920x1080 resolution, bluetooth  should be On, and you should always exit the PC settings with the x button or alt+F4. There is probably a solution to all of these but this is good enough for me:) 

I might generalize this to be more user friendly later.
