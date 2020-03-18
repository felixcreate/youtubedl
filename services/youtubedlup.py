#!/usr/bin/python3

import subprocess
import time

logfile = "/var/log/youtube/up.log"

outb = subprocess.check_output("/usr/local/bin/youtube-dl -U", shell = True, stderr=subprocess.STDOUT)
out = outb.decode()
#outl = out.split("\n")
#output = outl[0]

strline = "Ran at " + time.asctime() + " Eastern Time: "
strwrite = strline + out.replace("\n","") + "\n"
f = open(logfile, "a")
f.write(strwrite)
f.close()
