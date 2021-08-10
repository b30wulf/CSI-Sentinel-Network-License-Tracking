# CSI-Sentinel-Network-License-Tracking

This script communicates with lsmon.exe and lsmon.exe communicates with the Sentinel License Server. It will get the information, parse it for you, save it to license.html, and open the file for you.  


# How to use

To use this script, all you need is the CSILicense.bat, Parse.py, and writetohtm.py.
1. You need to edit the second line of CSILicense.bat to the address of lsmon.exe in your CSI Utilities. 
2. Change gs-5 to the name/ip of your server. 
3. Ensure all these files to your right should be in a folder together. 
4. Double click CSILicense.bat and you should have a webpage that pops up to tell you everything about your CSI network licenses.
