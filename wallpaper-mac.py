#python
# -*- coding: utf-8 -*-
#author amourjun

import os
import getpass
import random
import subprocess

file_dir = '/Volumes/work-1/platform/acg12'

print file_dir
#file_dir = ''

file = []

for root, dirs, files in os.walk(file_dir):
    for f in files:
        file.append(f)

cnt = 0
for f in file:
    print str(cnt) + '\t -- \t' + f
    cnt = cnt + 1

file_name = file_dir + '/' + file[random.randint(0, len(file) - 1)]

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

def set_wallpaper(file_name):
    subprocess.Popen(SCRIPT%file_name, shell = True)

set_wallpaper(file_name)