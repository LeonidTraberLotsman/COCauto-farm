import pyautogui as pg
import time
import os.path

file_path='D:\\Unity\\Repos\\COCauto-farm\\'

def ClickButton(Name, sec):
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
           pg.click()
           Found=True
        except Exception:
            
            print("Button "+Name+" not found")
        time.sleep(sec)

ClickButton(file_path+"BL.png",2)
#ClickButton(file_path+"B0.png",2)
ClickButton(file_path+"B1.png",1)
ClickButton(file_path+"B2.png",1)
time.sleep(2)
while(True):
    ClickButton(file_path+"B3.png",5)
   
    

    #time.sleep(5)
    #x, y = pg.locateCenterOnScreen(file_path+'Button3.png')
    #pg.moveTo(x,y)
    #pg.click()
    #time.sleep(2)