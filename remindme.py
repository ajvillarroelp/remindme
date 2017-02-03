#!/usr/bin/python
import os
import time
import sys
import subprocess
from gi.repository import Notify

APP = "RemindME"
BaseDir = os.environ['HOME']+"/.remindme"
CONFFILE = BaseDir + "/config.ini"
SLEEPINTERVAL = "7200"

# Utility funcs
# #########################################################


def notif_msg(msg):
    global BaseDir
    global APP
    icon = "remindme.png"
    n = Notify.Notification.new(APP, msg, icon)
    n.show()

###########################################################


#def usage():
#    print "Usage \n"

'''try:
    opts, args = getopt.getopt(sys.argv[1:], 'hs', ['help', 'setup'])
except getopt.GetoptError:
    usage()
    sys.exit(2)

for opt, arg in opts:
    if opt in ('-h', '--help'):
        usage()
        sys.exit(2)
    elif opt in ('-s', '--setup'):
        print "Setup...\n"
        DDIR = subprocess.check_output("zenity  --title \"Select Reminders file\" --file-selection")
        f = open(CONFFILE, "w")
        f.write("datadir="+DDIR+"\n")
        f.close()
        sys.exit(0)

debug = 0
if not os.path.exists(DATADIR):
    print "Directory "+DATADIR+" does not exists."
    sys.exit(2)
'''
###########################################
total = len(sys.argv)

if total > 1:
    if sys.argv[1] == "setup":
        print "Setup...\n"
        try:
            DATADIR = subprocess.check_output("zenity --title \"Select Reminders directory\" --file-selection --directory", shell=True)
            print "AA "+DATADIR
        except:
            print ""
        if DATADIR != "":
            f = open(CONFFILE, "w")
            f.write("datadir="+DATADIR+"\n")
            f.write("interval="+str(SLEEPINTERVAL)+"\n")
            f.close()
        else:
            print "Selection is empty...\nRun python remindme.py setup"
            sys.exit(2)
        if not os.path.exists(BaseDir):
            os.makedirs(BaseDir)
        os.system("cp listreminders.sh "+BaseDir)
        os.system("cp "+BaseDir+"/remindme.png ~/.icons")

# Read config parameters
try:
    DATADIR = subprocess.check_output("grep datadir "+CONFFILE+" | cut -d= -f 2", shell=True)
    DATADIR = DATADIR.rstrip('\n')
except:
    print "No config file specified!\n Run: python remindme.py setup"
    # DATADIR = os.environ['HOME']+"/Dropbox/Apps/My Notes in Gear/MyNotes"
    sys.exit(2)
if (DATADIR == "" or not os.path.isdir(DATADIR)) and total == 0:
    print "Notes Directory does not exists!\nRun python remindme.py setup"
    sys.exit(2)

try:
    SLEEPINTERVAL = subprocess.check_output("grep interval "+CONFFILE+" | cut -d= -f 2", shell=True)
except:
    SLEEPINTERVAL = "7200"

Notify.init(APP)


while (True):
    remindlist = list()
    try:
        output = subprocess.check_output("bash "+BaseDir+"/listreminders.sh", shell=True)
        tmplist = output.split(":")
        for item in tmplist:
            if item.rstrip() != "":
                remindlist.append(item.rstrip('\n'))
    except:
        print "No reminders"
    for item in remindlist:
        notif_msg(item.rstrip('\n'))
        time.sleep(7)
    # sys.exit(0)
    time.sleep(int(SLEEPINTERVAL))
