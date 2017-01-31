#!/usr/bin/python
import os
import sys
import time
import subprocess
import getopt

BaseDir = os.environ['HOME']+"/.remindme"
DATADIR = os.environ['HOME']+"/Dropbox/Apps/My Notes in Gear/MyNotes"
CONFFILE = BaseDir+"/config.ini"

# Utility funcs
# #########################################################


def notif_msg(msg):
    global BaseDir
    icon = BaseDir+"/remindme.png"
    os.system("notify-send -i "+icon+" RemindME \""+msg+"\"")
###########################################################


def usage():
    print "Usage \n"


try:
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

try:
    DATADIR = subprocess.check_output("grep datafile "+CONFFILE+" | cut -d= -f 2", shell=True)
    DATADIR = DATADIR.rstrip('\n')
except:
    print "No directory for reminders specified! Quiting..."
    sys.exit(2)

debug = 0
if not os.path.exists(DATADIR):
    print "Directory "+DATADIR+" does not exists."
    sys.exit(2)

###########################################


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
    time.sleep(2*3600)
