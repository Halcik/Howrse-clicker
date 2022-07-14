# -*- coding: utf-8 -*-
import pyautogui as pg
import time
import random
from feed import h_feed
from registration import h_registration
from groom_functions import h_groom, h_sleep
from next_horse import h_next
from death import death

import os

#Przerwa po kazdym wywolaniu pyautogui - tu 0,3 sekundy
pg.PAUSE = 0.3

n = int(input("Wpisz liczbę koni do oporządzenia:\n"))
v = int(input("Czy posiadasz vipa?\n 1-Tak\n 2-Nie\n"))
func_sleep = input("Czy mam kłaść spać? [y/n]\n")
print("Zaczynam")
#print("Zacznę oporządzać konie za 10 sekund.")
#time.sleep(10)
for i in range(n):
    #randomizacja czasu trwania przesunięcia myszki
    random.seed(a=None, version=2)
    r = random.uniform(0.1, 0.5)
    for j in range(2):
        time.sleep(1)
        #zwykłe oporządzenie
        h_registration( r)
        h_feed( r, v)
        h_groom( r)
        if func_sleep == "y" or func_sleep == "Y":
            h_sleep( r)
        death( r)
    print("Postęp:", i+1, "/", n)
    h_next( r)
#os.system('shutdown /s') #wyłącza kompa