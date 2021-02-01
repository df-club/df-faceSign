# Untitled - By: Lei Zhao - 周二 11月 10 2020

import os, lcd, image, utime

lcd.init()
lcd.rotation(2)
img = image.Image()

def draw_label(x, y, w, h, label, img):
    img.draw_rectangle(x,y,w,h,lcd.GREEN)
    img.draw_rectangle(x,y-3,w,13,lcd.GREEN,fill=True)
    img.draw_string(x+1,y-2,label)
    return img

# 显示已存储的头像和对应的姓名
with open("names.txt",'r') as f:
    record_names = f.read().splitlines()
    print(record_names)

x,y,w,h = 96,70,128,128
for i in range(len(record_names)):
    img.clear()
    image_id = i+1
    a = image.Image("/sd/image/"+str(image_id)+".jpg")
    img.draw_image(a,(x,y))
    label = str(image_id)+" "+record_names[i]
    #img.draw_rectangle(x,y-30,w+20,30,lcd.GREEN,fill=True)
    img.draw_string(x+2,y-30,label,scale=2)
    lcd.display(img)
    utime.sleep_ms(1000)

# 给图片重新标记命名
relabel = True
names = ['Bill Gates', 'Elon Musk','Jeff Bezos','Yun Ma','Huateng Ma','Yanhong Li','Jun Lei',
        'Shibo Xia','Yue Li','Lei Zhao','Qiangdong Liu','Yiming Zhang','Jiale Wang','Qinze Zheng',
        'Unknown','Unknown','Boyang Wang','Zhanghao Wang','Wenao Ma','YanHao Wang','Haorui Ma',
        'Yixuan Wang','Zixi Gao']
if relabel == True:
    with open("names.txt",'w') as f:
        for name in names:
            f.write(name+'\n')

with open("names.txt",'r') as f:
    record_names = f.read().splitlines()
    print(record_names)
