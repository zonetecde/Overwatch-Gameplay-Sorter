# get hero pic from https://overwatch.blizzard.com/en-us/heroes/

# from class="heroCardPortrait" slot="image" src=" to " style="--cardbg:url(

import urllib.request
import re
import os
from os import path

opener = urllib.request.FancyURLopener({})
url = "https://overwatch.blizzard.com/en-us/heroes/"
f = opener.open(url)
html = str(f.read())

# récupère les urls des photos# The string to search
urls_of_pic = re.findall(r'class="heroCardPortrait" slot="image" src="(.+?)" style="--cardbg:url\(', html)
name_of_heroes = re.findall(r'slot="gallery-items" url="/heroes/(.+?)" blz-toggled=""><blz-image class', html)

# download les images
if not path.exists('pic'):
    os.mkdir("pic")

i = 0
for image_url in urls_of_pic:
    opener = urllib.request.urlopen(image_url)
    img_data = opener.read()
    with open("pic/" + name_of_heroes[i] + '.png', 'wb') as handler:
        handler.write(img_data)
        
    i += 1