#!/usr/bin/python

############################        Imports        ############################

import sys
import os
import platform
import time
import webbrowser


############################       Pre-Sets        ############################

Author = 'Azlirn, GrenadeMagnet, ########'
Browser = 'chromium-browser'	# your favorite browser, 'firefox', 'chromium-browser' or 'windows-default'
Description = "Open a list of URLs in your browser"
Version = '0.1.7'

UrlsExample = '''
 www.google.com
 map.ipviking.com
 www.twitter.com
'''

##### SYS CHECKS #####

print "\n Running basic system checks..."
time.sleep(1)

##### Color Options #####
if platform.system() == 'win32' or platform.system() == 'win64':
	print " Color Options will be skipped on Windows Systems"
	# if windows, don't use colors
	(o,r,g,y,b,m,w,c,R,G,Y) = ('','','','','','','','','','','')
else:
	o 			= '\033[0m' 	#off
	r 			= '\033[31m' 	#red
	g 			= '\033[32m' 	#green
	y 			= '\033[33m' 	#yellow
	b 			= '\033[34m' 	#blue
	m 			= '\033[35m' 	#magenta
	w 			= '\033[37m' 	#white
	c			= '\033[1;38m'  #crimson
	R			= '\033[1;41m'  # Highlighted Red
	G 			= '\033[1;42m'  # Highlighted Green
	Y 			= '\033[1;43m'  # Highlighted Yellow
	print b, "You are running an OS compatible with colors!"
	time.sleep(1)


##### Check for a Compatible Operating System #####
print b, "Checking for compatible OS...", o
print y, "NOTE: Currently, only Linux Operating Systems Are Supported", o
time.sleep(1)

if platform.system() == 'win32' or platform.system() == 'win64':
	print r, "Program is not supported on Windows Operating Systems! Exiting Application...", o
	exit()
elif platform.system() == 'Linux':
	print g, "Looks like you are running a compatible OS! Continuing...\n", o
	time.sleep(1)

# Check for root privilages, exit if root is detected.
if platform.system() == 'Linux':
		if os.geteuid() == 0:
			print r, "Program will not run with root privilages! Exiting Application..."
			exit()

############################      Sub-Routines     ############################

##### Welcome Screen #####

print r, "\n -------------------------------------------------", o
print w, "----- Welcome to the SOC Text to URL Opener -----", o
print b, "-----            Written in 2015            -----", o
print w, "-----   By:%s  ----- "%(Author), o
print r, "-------------------------------------------------", o

print r," _____          _   _____  _   _______ _     _____				"
print w,"|_   _|        | | / __  \| | | | ___ \ |   |  _  |				"
print b,"  | | _____  _ | |_`' / /'| | | | |_/ / |   | | | |_ __   ___ _ __   ___ _ __	"
print r,"  | |/ _ \ \/ /  __| / /  | | | |    /| |   | | | | '_ \ / _ \ '_ \ / _ \ '__|	"
print w,"  | |  __/>  < | |_./ /___| |_| | |\ \| |___\ \_/ / |_) |  __/ | | |  __/ |	"
print b,"  \_/\___/_/\_\ \__\_____/ \___/\_| \_\_____/\___/| .__/ \___|_| |_|\___|_|	"
print r,"                                                 | |				"
print w,"                                                 |_|				"
print "\n"
print m, "This program is free software; however you can NOT redistribute it and/or"
print m, "modify it under any circumstances without the express written consent of"
print m, "at least one of the authors."

print m, "This program is distributed in the hope that it will be useful, but WITHOUT"
print m, "ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS"
print m, "FOR A PARTICULAR PURPOSE.", o

time.sleep(1)

############################      In Development     ############################

#### Define File ####
UrlFile = raw_input(' Please enter your file name, or file location: ')

############################      In Development     ############################

### User Chooses Browser ###

"""

print g, "Compatible Browsers"

browserChoice = {}
browserChoice['1']="Chromium"
browserChoice['2']="Firefox"
browserChoice['3']="Default"
broswerChoice['4']="Exit"
while True:
  options=menu.keys()
  options.sort()
    for entry in options:
      print entry, broswerChoice[entry]

    selection=raw_input("Please Select:")
    if selection =='1':
      print "Chromium"
    elif selection == '2':
      print "Firefox"
    elif selection == '3':
      print "Default"
    elif selection == '4':
      break
    else:
      print r, "Unknown Option Selected!"

"""



# Fault tolerant way to open text file
time.sleep(1)
try:
                dataFile = open(UrlFile,'r')
                print g, "\n", UrlFile, g,"loaded successfully!\n", o
except:
                print r, "\n ERROR - NO DATA IN FILE", o
		print b, "\n HERE IS SOME HELP:"
                print y, "Your file MUST be a text file."
                print y, "Each URL within your file MUST be on a new line.\n"
                print y, "example: \n", UrlsExample,
                print y, "\n NOTE: All URLs will open in the Chromium Browser by default.", o
		print r, "Exiting Application...", o
		time.sleep(1)
                exit()
time.sleep(1)

# Read each line and open it in a browser
for lines in dataFile:
  url = str(lines.strip())
  print b, "Opening a tab for " ,y + url, o
  webbrowser.get(Browser).open_new_tab(url)
  time.sleep(1)

#Close file and exit
print g, "\nText to URL Opener is finished.", o
time.sleep(1)
dataFile.close()
exit()


#############################   Revision History   ##############################

"""
0.1.7 - Added ASCII Art at start up. Moved system checks to the front of the script for efficiency. Added raw_input to allow user to specify text file to use.
0.1.6 - Removed windows compatibility for the time being to work out broswer configuration issues cross platform and added an operating system check. This feature will be introduced again in future versions.
0.1.5 - add user privilages check. Program will now terminate if user is root. Changed language of opening urls.
0.1.4 - add options for different browsers, since I don't have chromium on my windows PC
0.1.3 - colors (for linux). Who doesn't like colors?
0.1.2 - ######## added try / except for fault tolerance
0.1.1 - based on original Text2URL by Azlirn
"""

############################     Future Wishlist     #############################

"""
- Allow user to choose browser
- Create a variable called UrlFileLocation and add an if/else statement that will check the UrlFileLocation variable for a text file,
  if the text file in the UrlFile variable is not avaialble.
- add an argument that allows the user to view revision history and wishlist
- add a blank file checker with custom error

"""

############################          Notes          #############################

'''

'''

###########################          The End          ############################
