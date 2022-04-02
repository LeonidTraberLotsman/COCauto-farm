import pyautogui as pg
import random as r


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
    print("can find "+Name+" "+str(res))
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
    pg.moveTo(551,90)
    time.sleep(0.1)
    pg.click()
    #ClickButton(localpath+'g2.png',0.1,0)
    #while(CanFind(localpath+'g3.png')):
    pg.moveTo(405,825)
    pg.mouseDown()
    time.sleep(5)
    pg.mouseUp()
    pg.moveTo(1720,90)
    pg.click()

def ScanEnemies():
    t=True
    #ClickButton(file_path+"BL.png",2)
    #ClickButton(file_path+"B0.png",2)
    #Цикл боя
    while True:
        ClickButton(file_path+"B1.png",1,0)
        ClickButton(file_path+"B2.png",1,0)
        time.sleep(2)
        while True:
            if r.randint(0,2)==0:
                ClickButton(file_path+"B3.png",5,0)
            else:
                SpawnGoblins()
                break
        Hire()
        time.sleep(250)



def SpawnGoblins():
    GetToCorner()
    ClickButton(file_path+"attack/A0.png",0.1,0)
    while CanFind(file_path+"attack/A3.png"):
        for i in range(5):
            time.sleep(0.0001)
            x=r.randint(288,1655)
            y=r.randint(40,742)
            pg.moveTo(x,y)
            pg.click()
    ClickButton(file_path+"attack/A1.png",1,0)
    #1010,760
    #1274,244
    



    #time.sleep(5)
    #x, y = pg.locateCenterOnScreen(file_path+'Button3.png')
    #pg.moveTo(x,y)
    #pg.click()
time.sleep(2)
#Hire()
ScanEnemies()
#SpawnGoblins()
