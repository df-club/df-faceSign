# Untitled - By: Lei Zhao - 周五 11月 27 2020

import os, lcd, image, utime

lcd.init()
lcd.rotation(2)
img = image.Image()
record_names = []
record_ftrs = []

def loadInfo():
    # Load names info
    if "names.txt" in os.listdir():
        with open("names.txt",'r') as f:
            record_names[:] = f.read().splitlines()
    # Load features info
    if "ftrs.txt" in os.listdir():
        with open("ftrs.txt",'r') as f:
            record_ftrs[:] = f.read().split('\n|||||\n')
            record_ftrs.pop()

def printNames():
    for i in range(len(record_names)):
        print(i+1,':',record_names[i])

def showImageByID(image_id):
    x,y,w,h = 96,70,128,128
    img.clear()
    a = image.Image("/sd/image/"+str(image_id)+".jpg")
    img.draw_image(a,(x,y))
    label = str(image_id)+" "+record_names[image_id-1]
    img.draw_string(x+2,y-30,label,scale=2)
    lcd.display(img)

def renameByID(image_id, new_name):
    record_names[image_id-1] = new_name
    showImageByID(image_id)
    with open("names.txt",'w') as f:
        for name in record_names:
            f.write(name+'\n')

def delInfoByID(image_id):
    # delete name
    del_name = record_names.pop(image_id-1)
    print('Delete info:', image_id, '.', del_name)
    with open("names.txt",'w') as f:
        for name in record_names:
            f.write(name+'\n')
    # delete face image
    os.remove('/sd/image/'+str(image_id)+".jpg")
    # delete feature


def tmpRenameAllImages():
    for i in range(len(record_names)):
        old_name = '/sd/image/'+str(i+1)+".jpg"
        new_name = '/sd/image/'+record_names[i]+".jpg"
        print(old_name, '->', new_name)
        os.rename(old_name, new_name)

def showImages():
    x,y,w,h = 96,70,128,128
    for i in range(len(record_names)):
        image_id = i+1
        name = record_names[i]
        img.clear()
        a = image.Image("/sd/image/"+name+".jpg")
        img.draw_image(a,(x,y))
        label = str(image_id)+' '+record_names[i]
        img.draw_string(x+2,y-30,label,scale=2)
        lcd.display(img)
        utime.sleep_ms(1000)


#print(os.listdir('/sd/image'))
loadInfo()
printNames()
#tmpRenameAllImages()
showImages()
#showImageByID(10)
#renameByID(10, 'Lei Zhao')
