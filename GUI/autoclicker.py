import pyautogui as pg
import time

pg.press('win')
pg.typewrite('calculator',0.1)
pg.press('enter')

pg.moveTo(313,1400)

time.sleep(5)
pg.press('enter')