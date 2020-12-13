import pyautogui
import win32api, win32con
import time
from PIL import Image, ImageOps
from numpy import *

x_pad = 549
y_pad = 348

class clicks:
    small = 6
    medium = 8
    large = 10

class colors:
    noBowl = 4288
    smallBowl = 13813
    mediumBowl = 13003
    largeBowl = 9743

    canOrdersmall = 3969
    canOrdermedium = 5856
    canOrderlarge = 5639

    cannotOrderS = 3339
    cannotOrderM = 4847
    cannotOrderL = 4599

    end = 1430
    
class coords:
    startButton = (391, 336)
    clickRamen = (408, 490)
    bowlFinish= (662,523)

    orderSmall = (561, 113)
    orderMedium = (631, 113)
    orderLarge = (691, 113)

def main():
    startGame()
    time.sleep(2)
    while True:
        eating()
        ordering()
        check = isEnd()
        if check is True:
            break
        
def startGame():
    mousePos(coords.startButton)
    time.sleep(0.05)
    leftClick()
    
def isEnd():
    play_area = (x_pad + 44, y_pad + 225, 50, 25)
    myScreenshot = pyautogui.screenshot(region=(play_area))
    im = ImageOps.grayscale(myScreenshot)
    a = array(im.getcolors())
    a = a.sum()
    myScreenshot.save(r'C:\Users\Joshua\Desktop\拉麵大胃王\screenshot1.png')

    if a == colors.end:
        return True
    else:
        return False


def ordering():
    availability = checkmenuLarge()
    if availability != colors.cannotOrderL:
        mousePos(coords.orderLarge)
        time.sleep(0.01)
        leftClick()
        time.sleep(0.01)
        

    availability = checkmenuMedium()
    if availability != colors.cannotOrderM:
        mousePos(coords.orderMedium)
        time.sleep(0.01)
        leftClick()
        time.sleep(0.01)


    availability = checkmenuSmall()
    if availability != colors.cannotOrderS:
        mousePos(coords.orderSmall)
        time.sleep(0.01)
        leftClick()
        time.sleep(0.01)

    availability = 0

    
def eating():
    mousePos(coords.clickRamen)
    bowlSize = isBowl()

    if bowlSize == colors.smallBowl:
        for i in range(clicks.small):
            leftClick()
            time.sleep(.001)
        leftDown()
        mousePos(coords.bowlFinish)
        leftUp()
            
    elif bowlSize == colors.mediumBowl:
        for i in range(clicks.medium):
            leftClick()
            time.sleep(.01)
        leftDown()
        mousePos(coords.bowlFinish)
        leftUp()
            
    elif bowlSize == colors.largeBowl:
        for i in range(clicks.large):
            leftClick()
            time.sleep(.01)
        leftDown()
        mousePos(coords.bowlFinish)
        leftUp()
        
    elif bowlSize != colors.noBowl:
        for i in range(clicks.large):
            leftClick()
            time.sleep(.01)
        leftDown()
        mousePos(coords.bowlFinish)
        leftUp()
    
    else:
        ordering()
    
        
def checkmenuLarge():
    play_area = (x_pad + 677, y_pad + 60, 42, 28)
    myScreenshot = pyautogui.screenshot(region=(play_area))
    im = ImageOps.grayscale(myScreenshot)
    a = array(im.getcolors())
    a = a.sum()
    myScreenshot.save(r'C:\Users\Joshua\Desktop\拉麵大胃王\screenshot1.png')
    return a

def checkmenuMedium():
    play_area = (x_pad + 612, y_pad + 60, 42, 28)
    myScreenshot = pyautogui.screenshot(region=(play_area))
    im = ImageOps.grayscale(myScreenshot)
    a = array(im.getcolors())
    a = a.sum()
    myScreenshot.save(r'C:\Users\Joshua\Desktop\拉麵大胃王\screenshot1.png')
    return a

def checkmenuSmall():
    play_area = (x_pad + 543, y_pad + 60, 42, 28)
    myScreenshot = pyautogui.screenshot(region=(play_area))
    im = ImageOps.grayscale(myScreenshot)
    a = array(im.getcolors())
    a = a.sum()
    myScreenshot.save(r'C:\Users\Joshua\Desktop\拉麵大胃王\screenshot1.png')
    return a

def isBowl():
    play_area = (x_pad + 383, y_pad + 493, 52, 40)
    myScreenshot = pyautogui.screenshot(region=(play_area))
    im = ImageOps.grayscale(myScreenshot)
    a = array(im.getcolors())
    a = a.sum()
    myScreenshot.save(r'C:\Users\Joshua\Desktop\拉麵大胃王\screenshot1.png')
    return a

def screenGrab():
    play_area = (x_pad + 1, y_pad + 1, 799, 600)
    myScreenshot = pyautogui.screenshot(region=(play_area))
    myScreenshot.save(r'C:\Users\Joshua\Desktop\拉麵大胃王\screenshot1.png')
    return myScreenshot

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
 
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)


def mousePos(coord):
    win32api.SetCursorPos((x_pad + coord[0],y_pad + coord[1]))

