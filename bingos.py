from PIL import Image , ImageDraw , ImageFont
from random import randrange
from datetime import datetime

import random
import os

font = ImageFont.truetype("arial_black.ttf",100)

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y-%H-%M-%S")
os.mkdir('./'+timestampStr)

file = open("./"+timestampStr+"/bingos" + timestampStr + ".txt", "w")
mul=270
h=290
v=40
a=650#580
r=250
cant=int(input("Ingrese la cantidad de bingos a generar: "))



for c in range(cant):
    
    image = Image.open('img/carta.png')

    b=random.sample(range(1, 16), 5)
    ii=random.sample(range(16, 31), 5)
    n=random.sample(range(31, 46), 5)
    g=random.sample(range(46, 61), 5)
    o=random.sample(range(61, 76), 5)

    numbers = [
        random.sample(range(1, 16), 5),
        random.sample(range(16, 31), 5),
        random.sample(range(31, 46), 5),
        random.sample(range(46, 61), 5),
        random.sample(range(61, 76), 5),
    ]

    print(numbers)
    d = ImageDraw.Draw(image)

    for i in range(1,6):
        for y in range(1,6):
            """
            if i==1:
                if b[y-1]<10:
                    d.text((r+30,a), str(b[y-1]), font=font,fill=(255,255,255))
                else:
                    d.text((r,a), str(b[y-1]), font=font,fill=(255,255,255))
            if i==2:
                d.text((r,a), str(ii[y-1]), font=font,fill=(255,255,255))
            if i==3:
                if y==3:
                    d.text((r,a), "", font=font,fill=(255,255,0))
                else:
                    d.text((r,a), str(n[y-1]), font=font,fill=(255,255,255))
            if i==4:
                d.text((r,a), str(g[y-1]), font=font,fill=(255,255,255))
            if i==5:
                d.text((r,a), str(o[y-1]), font=font,fill=(255,255,255))
            """
            if i==1 and numbers[0][y-1]<10:
                d.text((r+30,a), str(numbers[0][y-1]), font=font,fill=(255,255,255))
            elif i==1:
                d.text((r,a), str(numbers[0][y-1]), font=font,fill=(255,255,255))
            elif i==2:
                d.text((r,a), str(numbers[1][y-1]), font=font,fill=(255,255,255))
            elif i==3 and y!=3:
                d.text((r,a), str(numbers[2][y-1]), font=font,fill=(255,255,255))
            elif i==3 and y==3:
                d.text((r,a), "", font=font,fill=(255,255,0))
            elif i==4:
                d.text((r,a), str(numbers[3][y-1]), font=font,fill=(255,255,255))
            elif i==5:
                d.text((r,a), str(numbers[4][y-1]), font=font,fill=(255,255,255))

            a=a+260
        a=650
        r=r+255
    a=650
    r=250
    image.save('./'+timestampStr+'/bingo' + str('{:0>3}'.format(c))+ '.png')

    file.write('bingo' + str('{:0>3}'.format(c)) + os.linesep)
    file.write("B   I   N   G   O" + os.linesep)
    cc=1
    for k in range(1,6):
        if k==3:
            if cc==3 and b[k-1]<10:
                file.write(str(b[k-1])+ "   " + str(ii[k-1])+ "      "  + str(g[k-1])+ "  " + str(o[k-1])+ "  " + os.linesep)
            else:
                file.write(str(b[k-1])+ "  " + str(ii[k-1])+ "      "  + str(g[k-1])+ "  " + str(o[k-1])+ "  " + os.linesep)
        elif b[k-1]<10:
            file.write(str(b[k-1])+ "   " + str(ii[k-1])+ "  " + str(n[k-1])+ "  " + str(g[k-1])+ "  " + str(o[k-1])+ "  " + os.linesep)
        else:
            file.write(str(b[k-1])+ "  " + str(ii[k-1])+ "  " + str(n[k-1])+ "  " + str(g[k-1])+ "  " + str(o[k-1])+ "  " + os.linesep)
        cc=cc+1
    file.write("--------------------------------" + os.linesep)
    print("Bingo " + str('{:0>3}'.format(c))+ " generado")
file.close()

