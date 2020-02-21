#!/usr/bin/python3

import sys
import uuid
import os
import subprocess
from os import path
import smtplib
import ssl
from datetime import datetime

sender_email = "felixserverinfo@gmail.com"
receiver_email = "felixfbpuppy@gmail.com"
password = "fesserverinfo"
context = ssl.create_default_context()
base = "Subject: Youtube-dl error at {0:%H:%M} ({0:%I:%M %p})\n\nYoutube-dl encontered an error on {0:%a, %b %d %Y} at {0:%H:%M} ({0:%I:%M %p}) with youtube url {1}:\n\n"

url = sys.argv[1]

f = open("/var/www/youtube-backend/log.txt", "r")
match = 0
for x in f:
    l = x.split()
    if(l[0] == url):
        m = l[1]
        match = 1
        break
f.close()

if(match == 0):
    nuuid = uuid.uuid4()
    name = str(nuuid) + ".mp4"
    youout = subprocess.check_output("/usr/local/bin/youtube-dl --quiet --no-mtime -f mp4 --output /var/www/youtube-backend/file/"+ name + " " + url + "; exit 0", shell=True, stderr=subprocess.STDOUT)
    curtime = datetime.now()
    if(path.exists("/var/www/youtube-backend/file/" + name)):
        f = open("/var/www/youtube-backend/log.txt", "a")
        f.write(url + " " + name + " " + curtime.isoformat() + '\n')
        f.close()
        print(name)
    else:
        yououtput = youout.decode()
        message = base.format(curtime, url) + yououtput
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        server.close()
        print("error")
else:
    print(m)
