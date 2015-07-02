# README #

## Text2UrlOpener ##
## Ver - 0.1.7 ##

This is a Python based tool developed to open multiple URLs in a text file.

### How do I get set up? ###

**Summary of set up:**

This program has a configurable area where users can specify the browser to be used along with other minor details.

Users will need to ensure they know the location of the text file they will be using for this program. The default storage location of the text file is the same location of the script itself. There is a separate variable already configured in this script if your file location differs. Simply input your file location into the commented out variable. Ensure to comment out the original UrlFile variable if you choose to go with this set up.

**Configuration:**

Users will need to be running Python 2.7.x in order to use this program.

**Dependencies:**

Currently the only browser that has been tested is Chromium.  

Versions 0.1.6 and 0.1.7 are only compatible with Linux operating systems. If you are running Windows, you will need to use Ver. 0.1.5 and older.
To check your current system, run the following snippet


```
#!/usr/bin/python

##### Imports #####

import platform
import sys
import os

##### Variables for Platform #####
operatingSystem = platform.system()
machine = platform.machine()
networkNode = platform.node()
processor = platform.processor()
UserID = os.geteuid()

##### Sub-Routines #####
print "Your are currently running ", operatingSystem
print "Your machine type is ", machine
print "You processor is a ", processor
print "Your Network Node name is ", networkNode
print "Your access level is", UserID
exit()

##### END #####

```

### Revision History ###

0.1.7 - Added ASCII Art at start up. Moved system checks to the front of the script for efficiency. Added raw_input to allow user to specify text file to use.

0.1.6 - Removed windows compatibility for the time being to work out browser configuration issues cross platform and added an operating system check. This feature will be introduced again in future versions.

0.1.5 - add user privileges check. Program will now terminate if user is root. Changed language of opening urls.

0.1.4 - add options for different browsers, since I don't have chromium on my windows PC

0.1.3 - colors (for linux). Who doesn't like colors?

0.1.2 - ######## added try / except for fault tolerance

0.1.1 - based on original Text2URL by ######
