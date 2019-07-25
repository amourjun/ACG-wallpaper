# ACG-wallpaper
初学python，之前想抓取P站的一些图片来着，然后发现acg12这里有专门的壁纸榜单，就写了个抓取壁纸作为mac桌面壁纸玩玩。
功能：抓取acg12壁纸榜单的动漫壁纸，并定时随机设定为桌面壁纸

 - v1: 暂时完成两个脚本并且分步执行；1、生成acg12文件夹并抓取定额壁纸到本地。2、读取壁纸文件夹，随机选择一张壁纸调用appleScript设置桌面壁纸。

#spider.py
完成图片抓取功能，由于acg12中的url格式规律很好找，只需要找到图片存放的url规律就行，这里用urilib的那个下载函数失败了，就换成wirte直接写入文件了，并且用了多线程加快下载速度。因为线程之间没冲突，所以不需要用到异步锁。过程中学习了python的语法以及相关特性。
```python { .theme-legacy }
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
```


#wallpaper-mac.py
将指定文件夹中的非目录文件加入file列表，通过随机函数随机选取壁纸文件，并通过调用applesScript脚本来设置mac壁纸。
这里暂时只实现了mac版本，后续进行兼容到windows版本，并且将整个项目打包。
```python { .theme-legacy }
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
```


