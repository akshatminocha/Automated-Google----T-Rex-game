from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *


class Coordinates():
    replayBtn=(340,390)   #these are coordinates of replay button, not the pixels and are relative to my screen size
    dinosaur=(171,395)    #these are coordinates of dinosaur, not the pixels and are relative to my screen size

def restartGame():
    pyautogui.click(Coordinates.replayBtn)
    

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')
    
    
#restartGame()
#time.sleep(1)
#pressSpace()

def imageGrab():
    box=(Coordinates.dinosaur[0]+60,Coordinates.dinosaur[1],Coordinates.dinosaur[0]+100,Coordinates.dinosaur[1]+30)
    image=ImageGrab.grab(box)
    grayImage=ImageOps.grayscale(image)
    a=array(grayImage.getcolors())
    print(a.sum())
    return a.sum()
    
def main():
    restartGame()
    while True:       
        if(imageGrab()!=1530):
            pressSpace()
            time.sleep(0.1)
                      
main()   


   
    
    
    
