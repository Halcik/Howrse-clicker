import pyautogui as pg
import random, time, os

#Karmienie
def h_feed( r, v, path_project):
    feeding = pg.locateOnScreen(os.path.join(path_project, 'Image', 'Feed.JPG'), confidence=0.9)
    care = pg.locateOnScreen(os.path.join(path_project, 'Image', 'Care.JPG'), confidence=0.9)

    if feeding:
        feeded = pg.locateOnScreen(os.path.join(path_project, 'Image', 'feeded.JPG'), confidence=0.9)
        while feeded is None:
            if feeding:
                left, top, right, down = feeding[0], feeding[1], feeding[0]+feeding[2], feeding[1]+feeding[3]
                pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
                pg.click()
            feed_it = pg.locateOnScreen(os.path.join(path_project, 'Image', 'Feeding.JPG'), confidence=0.8)
            if(feed_it != None):
                left, top, right, down = feed_it[0], feed_it[1], feed_it[0]+feed_it[2], feed_it[1]+feed_it[3]
                pg.moveTo(random.uniform(left+2, right-2), random.uniform(top-2, down+2), r, pg.easeOutQuad)
                pg.click()
            time.sleep(0.3)
            feeding = pg.locateOnScreen(os.path.join(path_project, 'Image', 'Feed.JPG'), confidence=0.9)
            feeded = pg.locateOnScreen(os.path.join(path_project, 'Image', 'feeded.JPG'), confidence=0.9)

    elif care:
        left, top, right, down = care[0], care[1], care[0]+care[2], care[1]+care[3]
        pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
        pg.click()
    
    if v != 1 and care == None and feeding: #tego na razie nie ruszam D: another time - I have to write it again
        try:
            feed0 = pg.locateCenterOnScreen('Image/Feed0.JPG', confidence=0.93)
            print("0: ", feed0)
            if feed0:
                quantity = pg.locateCenterOnScreen('Image/quantity0.JPG', confidence=0.9)
                pg.moveTo(quantity.x, quantity.y, r, pg.easeOutQuad)
            else:
                raise ErrorFeed()

        except ErrorFeed:
            try:
                feed20 = pg.locateCenterOnScreen('Image/Feed20.JPG', confidence=0.9)
                print("20: ", feed20)
                if feed20:
                    pg.move(196, 172, r, pg.easeOutQuad)
                else:
                    raise ErrorFeed()

            except ErrorFeed:
                try:
                    feed12 = pg.locateCenterOnScreen('Image/Feed12.JPG', confidence=0.9)
                    print("12: ", feed12)
                    if feed12:
                        pg.move(107, 88 , r, pg.easeOutQuad)
                    else:
                        feed12 = pg.locateCenterOnScreen('Image/Feed12_2.JPG', confidence=0.9)
                        print("12_2: ", feed12)
                        if feed12:
                            pg.move(107, 88 , r, pg.easeOutQuad)
                        else:
                            raise ErrorFeed()

                except ErrorFeed:
                    try:
                        feed10 = pg.locateCenterOnScreen('Image/Feed10.JPG', confidence=0.9)
                        print("10: ", feed10)
                        if feed10:
                            pg.move(85, 88, r, pg.easeOutQuad)
                        else:
                            feed10 = pg.locateCenterOnScreen('Image/Feed10_2.JPG', confidence=0.9)
                            print("10_2: ", feed10)
                            if feed10:
                                pg.move(85, 88, r, pg.easeOutQuad)
                            else:
                                raise ErrorFeed()

                    except ErrorFeed:
                        try:
                            feed8 = pg.locateCenterOnScreen('Image/Feed8.JPG', confidence=0.9)
                            print("8: ", feed8)
                            if feed8:
                                pg.move(64, 88, r, pg.easeOutQuad)
                            else:
                                feed8 = pg.locateCenterOnScreen('Image/Feed8_2.JPG', confidence=0.9)
                                print("8_2: ", feed10)
                                if feed8:
                                    pg.move(64, 88, r, pg.easeOutQuad)
                                else:
                                    raise ErrorFeed()

                        except ErrorFeed:
                            try:
                                feed4 = pg.locateCenterOnScreen('Image/Feed4.JPG', confidence=0.9)
                                print("4: ", feed4)
                                if feed4:
                                    pg.move(21, 88, r, pg.easeOutQuad)
                                else:
                                    raise ErrorFeed()

                            except ErrorFeed:
                                try:
                                    feed14 = pg.locateCenterOnScreen('Image/Feed14.JPG', confidence=0.9)
                                    print("14: ", feed14)
                                    if feed14:
                                        pg.move(130, 88, r, pg.easeOutQuad)
                                    else:
                                        raise ErrorFeed()

                                except ErrorFeed:
                                    try:
                                        feed6 = pg.locateCenterOnScreen('Image/Feed6.JPG', confidence=0.9)
                                        print("6: ", feed6)
                                        if feed6:
                                            pg.move(42, 88, r, pg.easeOutQuad)
                                        else:
                                            feed6 = pg.locateCenterOnScreen('Image/Feed6_2.JPG', confidence=0.9)
                                            print("6_2: ", feed6)
                                            if feed6:
                                                pg.move(42, 88, r, pg.easeOutQuad)
                                            else:
                                                raise ErrorFeed()

                                    except ErrorFeed:
                                        try:
                                            feed16 = pg.locateCenterOnScreen('Image/Feed16.JPG', confidence=0.93)
                                            print("16: ", feed16)
                                            if feed16:
                                                pg.move(152, 88, r, pg.easeOutQuad)
                                            else:
                                                raise ErrorFeed()

                                        except:
                                            pg.move(107, 88 , r, pg.easeOutQuad)
                                            print("Zastosowano alternatywę")

        finally:
            pg.click()
            feed_it = pg.locateOnScreen('Image/Feeding.JPG', confidence=0.8)
            if(feed_it != None):
                left, top, right, down = feed_it[0], feed_it[1], feed_it[0]+feed_it[2], feed_it[1]+feed_it[3]
                pg.moveTo(random.uniform(left+2, right-2), random.uniform(top-2, down+2), r, pg.easeOutQuad)
                pg.click()

#Oporządzenie
def h_groom( r, path_project):
    groom = pg.locateOnScreen(os.path.join(path_project, 'Image', 'Groom.JPG'), confidence=0.9)
    groom2 = pg.locateOnScreen(os.path.join(path_project, 'Image', 'Groom2.JPG'), confidence=0.9)

    if groom:
        left, top, right, down = groom[0], groom[1], groom[0]+groom[2], groom[1]+groom[3]
        pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
        pg.click()
    elif groom2:
        left, top, right, down = groom2[0], groom2[1], groom2[0]+groom2[2], groom2[1]+groom2[3]
        pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
        pg.click()

# Polozenie spac
def h_sleep( r, path_project):
    sleep_horse = pg.locateOnScreen(os.path.join(path_project, 'Image', 'Sleep.JPG'), confidence=0.8)

    if sleep_horse:
        left, top, right, down = sleep_horse[0], sleep_horse[1], sleep_horse[0]+sleep_horse[2], sleep_horse[1]+sleep_horse[3]
        pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
        pg.click()

# Przejście do następnego konia
def h_next( r, path_project):
    n_horse = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'Arrow.jpg'), confidence=0.9)
    
    if n_horse:
        pg.moveTo(n_horse.x, n_horse.y, r, pg.easeOutQuad)
        pg.click()
    
    else:
        n_horse = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'Arrow2.JPG'), confidence=0.9)
        if n_horse:
            pg.moveTo(n_horse.x, n_horse.y, r, pg.easeOutQuad)
            pg.click()
        else:
            n_horse = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'Arrow4.JPG'), confidence=0.9)
            if n_horse:
                pg.moveTo(n_horse.x, n_horse.y, r, pg.easeOutQuad)
                pg.click()
            else:
                n_horse = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'Arrow3.JPG'), confidence=0.9)
                if n_horse:
                    pg.moveTo(n_horse.x, n_horse.y, r, pg.easeOutQuad)
                    pg.click()
                else:
                    n_horse = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'Arrow5.JPG'), confidence=0.9)
                    if n_horse:
                        pg.moveTo(n_horse.x, n_horse.y, r, pg.easeOutQuad)
                        pg.click()
                    else:
                        n_horse = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'Arrow6.JPG'), confidence=0.9)
                        if n_horse:
                            pg.moveTo(n_horse.x, n_horse.y, r, pg.easeOutQuad)
                            pg.click()
                        else:
                            print("Wystąpił błąd z przechodzeniem do następnego konia")
                            pg.press('f5')
                            time.sleep(1.5)
                            pg.click()



class ErrorFeed(Exception):
    pass