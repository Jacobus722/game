from PIL import Image
import random
from bisect import bisect

greyscale = [
            " ",
            " ",
            ".,-",
            "_ivc=!/|\\~",
            "gjez2]/(YL)t[+T7Vf",
            "mdK4ZGbNDXY5P*Q",
            "W8KMA",
            "#%$"
            ]

zonebounds=[36,72,108,144,180,216,252]

im=Image.open(r"c:\test.jpg")
im=im.resize((160, 75),Image.BILINEAR)
im=im.convert("L") # convert to mono

str=""
for y in range(0,im.size[1]):
    for x in range(0,im.size[0]):
        lum=255-im.getpixel((x,y))
        row=bisect(zonebounds,lum)
        possibles=greyscale[row]
        str=str+possibles[random.randint(0,len(possibles)-1)]
    str=str+"\n"
 
print str