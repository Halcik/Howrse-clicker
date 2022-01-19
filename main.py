# -*- coding: utf-8 -*-
from pickle import FALSE
from types import NoneType
import pyautogui
import time
import random

#Przerwa po kazdym wywolaniu pyautogui - tu 0,5 sekundy
pyautogui.PAUSE = 0.5

# Zarejestrowanie w osrodku
def h_registration():
    registration = pyautogui.locateCenterOnScreen('Image\Registration.jpg', confidence=0.9)
    if(registration != None):
        pyautogui.moveTo(registration.x, registration.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
        time.sleep(3.0)
        h_registration2()
    else:
        return
    
def h_registration2():
    reserved = pyautogui.locateCenterOnScreen('Image\Reserved.jpg', confidence=0.8)
    if(reserved != None):
        pyautogui.moveTo(reserved.x, reserved.y, r, pyautogui.easeOutQuad)
        pyautogui.click()

        box = pyautogui.locateCenterOnScreen('Image\Box.jpg', confidence=0.8, grayscale=False)
        pyautogui.moveTo(box.x, box.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
        feeding = pyautogui.locateCenterOnScreen('Image\Feed.jpg', confidence=0.9)
        if(box == None and feeding == None):
            print("Wystąpił błąd rejestrowania")
            pyautogui.press('f5')
            h_registration2()
        else:
            pass
    else:
        r_days = pyautogui.locateCenterOnScreen('Image\Days.jpg', confidence=0.9)
        if(r_days != None):
            pyautogui.moveTo(r_days.x, r_days.y, r, pyautogui.easeOutQuad)
            pyautogui.click()
            r_price = pyautogui.locateCenterOnScreen('Image\Price.jpg', confidence=0.9, grayscale=False)
            pyautogui.moveTo(r_price.x, r_price.y, r, pyautogui.easeOutQuad)
            pyautogui.click()
        else:
            pass

# Nakarmienie
def h_feed():
    feeding = pyautogui.locateCenterOnScreen('Image\Feed.jpg', confidence=0.9)
    care = pyautogui.locateCenterOnScreen('Image\Care.jpg', confidence=0.9)
    if (feeding != None):
        pyautogui.moveTo(feeding.x, feeding.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
    elif (care != None):
        pyautogui.moveTo(care.x, care.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
    else:
        return
    
    if (v != 1):
        Feed14 = pyautogui.locateCenterOnScreen('Image\Feed14.jpg', confidence=0.9)
        #print("14: ", Feed14)

        Feed12 = pyautogui.locateCenterOnScreen('Image\Feed12.jpg', confidence=0.9)
       # print("12: ", Feed12)

        Feed10 = pyautogui.locateCenterOnScreen('Image\Feed10.jpg', confidence=0.93)
        #print("10: ", Feed10)

        Feed8 = pyautogui.locateCenterOnScreen('Image\Feed8.jpg', confidence=0.9)
        #print("8: ", Feed8)

        Feed20 = pyautogui.locateCenterOnScreen('Image\Feed20.jpg', confidence=0.9)
        #print("20: ", Feed20)

        Feed6 = pyautogui.locateCenterOnScreen('Image\Feed6.jpg', confidence=0.9)
       # print("6: ", Feed6)

        Feed16 = pyautogui.locateCenterOnScreen('Image\Feed16.jpg', confidence=0.93)
        #print("16: ", Feed16)

        Feed0 = pyautogui.locateCenterOnScreen('Image\Feed0.jpg', confidence=0.93)
        #print("0: ", Feed0)

        if(Feed20 != None):
            quantity = pyautogui.locateCenterOnScreen('Image\quantity20.jpg', confidence=0.95)
            pyautogui.moveTo(quantity.x, quantity.y, r, pyautogui.easeOutQuad)
        elif(Feed0 != None):
            quantity = pyautogui.locateCenterOnScreen('Image\quantity0.jpg', confidence=0.9)
            pyautogui.moveTo(quantity.x, quantity.y, r, pyautogui.easeOutQuad)
            pyautogui.click()
            return
        elif(Feed12 != None):
            quantity = pyautogui.locateCenterOnScreen('Image\quantity12.jpg', confidence=0.95)
            pyautogui.moveTo(quantity.x, quantity.y, r, pyautogui.easeOutQuad)
        elif(Feed10 != None):
            quantity = pyautogui.locateCenterOnScreen('Image\quantity10.jpg', confidence=0.95)
            pyautogui.moveTo(quantity.x, quantity.y, r, pyautogui.easeOutQuad)
        elif(Feed8 != None):
            quantity = pyautogui.locateCenterOnScreen('Image\quantity8.jpg', confidence=0.95)
            pyautogui.moveTo(quantity.x, quantity.y, r, pyautogui.easeOutQuad)
        elif(Feed14 != None):
            quantity = pyautogui.locateCenterOnScreen('Image\quantity14.jpg', confidence=0.95)
            pyautogui.moveTo(quantity.x, quantity.y, r, pyautogui.easeOutQuad)
        elif(Feed6 != None):
            quantity = pyautogui.locateCenterOnScreen('Image\quantity6.jpg', confidence=0.95)
            pyautogui.moveTo(quantity.x, quantity.y, r, pyautogui.easeOutQuad)
        elif(Feed16 != None):
            quantity = pyautogui.locateCenterOnScreen('Image\quantity16.jpg', confidence=0.95)
            pyautogui.moveTo(quantity.x, quantity.y, r, pyautogui.easeOutQuad)
        else:
            pass
        
        pyautogui.click()
    else:
        pass

    feed_it = pyautogui.locateCenterOnScreen('Image\Feeding.jpg', confidence=0.8)
    if(feed_it != None):
        pyautogui.moveTo(feed_it.x, feed_it.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
    else:
        pass
 
# Oporzadzenie
def h_groom():
    groom = pyautogui.locateCenterOnScreen('Image\Groom.jpg', confidence=0.9)
    if(groom != None):
        pyautogui.moveTo(groom.x, groom.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
    else:
        return

# Polozenie spac
def h_sleep():
    sleep_horse = pyautogui.locateCenterOnScreen('Image\Sleep.jpg', confidence=0.8)
    if(sleep_horse != None):
        pyautogui.moveTo(sleep_horse.x, sleep_horse.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
    else:
        return

# Przejscie do nastepnego konia
def h_next():
    n_horse = pyautogui.locateCenterOnScreen('Image\Arrow.jpg', confidence=0.9)
    n_horse2 = pyautogui.locateCenterOnScreen('Image\Arrow2.jpg', confidence=0.9)
    if(n_horse != None):
        pyautogui.moveTo(n_horse.x, n_horse.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
    elif (n_horse2 != None):
        pyautogui.moveTo(n_horse2.x, n_horse2.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
    else:
        print("Wystąpił błąd z przechodzeniem do następnego konia")
        pyautogui.press('f5')
        h_next()

print("Wpisz liczbę koni do oporządzenia:")
n = int(input())
print("Czy posiadasz vipa?\n 1-Tak\n 2-Nie")
v = int(input())
print("Zacznę oporządzać konie za 15 sekund.")
time.sleep(15)
duration = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,]
for x in range(n):
    #randomizacja czasu trwania przesunięcia myszki
    random.seed(a=None, version=2)
    r = random.choice(duration)
    for y in range(2):
        #zwykłe oporządzenie
        h_registration()
        h_feed()
        h_groom()
        h_sleep()
    print("Postęp:", x+1, "/", n)
    h_next()
    