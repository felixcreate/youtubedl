#!/usr/bin/python3

from datetime import datetime
from os import listdir, path, remove

currenttime = datetime.now()
epochtime = currenttime.timestamp()
files = listdir("file/")
video2del = []
audio2del = []
vidaftertext = ""
audaftertext = ""

for x in files:
    t = path.getctime("file/" + x)
    if((epochtime - t) > 43200):
        if(x[-3:] == "mp4"):
            video2del.append(x)
        else:
            audio2del.append(x)
        remove("file/" + x)

logf = open("log.txt", "r")

for y in logf:
    l = y.split(" ")
    if not any(v in l[1] for v in video2del):
        vidaftertext += y
logf.close()

logaf = open("loga.txt", "r")

for z in logaf:
    la = z.split(" ")
    if not any(a in la[1] for a in audio2del):
        audaftertext += z
logaf.close()

logf = open("log.txt", "w")
logf.write(vidaftertext)
logf.close()

logaf = open("loga.txt", "w")
logaf.write(audaftertext)
logaf.close()

print(vidaftertext)
print(audaftertext)
print(video2del)
print(audio2del)