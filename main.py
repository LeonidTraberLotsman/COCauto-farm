import pyautogui as pg


import time
import os.path

file_path='D:\\Unity\\Repos\\COCauto-farm\\'



def ClickButton(Name, sec, pushTime):
    Found=False
    if(not(os.path.exists(Name))):
        print("file "+Name+" don't exist")
        return
    else:
        print("file "+Name+" exist")

    while(not Found):
        try:
           print("A")
           x, y = pg.locateCenterOnScreen(Name)
           print("B")

           print(x)
           print(y)
           pg.moveTo(x,y)
           if pushTime==0:
            pg.click()
           else:
               pg.mouseDown()
               time.sleep(pushTime)
               pg.mouseUp()
           Found=True
        except Exception:
            
            print("Button "+Name+" not found")
        time.sleep(sec)
def CanFind(Name):
    res=True
    try:  
        x, y = pg.locateCenterOnScreen(Name)  
    except Exception:
            res=False
    return res




def GetToCorner():
    pg.keyDown('S')
    pg.keyDown('A')
    time.sleep(0.5)
    pg.keyUp('A')
    pg.keyUp('S')

def Hire():
    localpath=file_path+'goblin\\'
    while(not CanFind(file_path+"B1.png")):
        time.sleep(0.1)
    GetToCorner()
    ClickButton(localpath+'g1.png',0.1,0)
    ClickButton(localpath+'g2.png',0.1,0)
    while(CanFind(localpath+'g3.png')):
        ClickButton(localpath+'g3.png',0.1,7)
    ClickButton(localpath+'g4.png',0.1,0)

def ScanEnemies():
    #ClickButton(file_path+"BL.png",2)
    #ClickButton(file_path+"B0.png",2)
    ClickButton(file_path+"B1.png",1,0)
    ClickButton(file_path+"B2.png",1,0)
    time.sleep(2)
    while(True):
        ClickButton(file_path+"B3.png",5,0)
   


    #time.sleep(5)
    #x, y = pg.locateCenterOnScreen(file_path+'Button3.png')
    #pg.moveTo(x,y)
    #pg.click()
    #time.sleep(2)