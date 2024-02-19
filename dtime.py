import datetime as dt
import time
import playsound
import pygame

current_date = dt.datetime.now()
# print(current_date)

# ==== HOWW TO SET DATETIME =================

set_dt = dt.datetime(2024, 2, 19, 6,55,34,333)
# print(set_dt)

# strftime
_time = dt.datetime.now()
# print(_time.strftime('%B'))

# day = %a or %A
# month = %b or %B
# year = %y or %Y
# AM/PM = %p or %P
# 24hrs = %H
# 12hrs = %I
# 
# =================== ALARM SYSTEM ==========================
# try:
#     playsound.playsound('C:\python-level-two\music\Greatman_Takit_-_Correct_CeeNaija.com'.mp3)
# except TypeError:
#     print('Music not loadable')

# ================== PYGAME ============================
pygame.init()
pygame.mixer.music.load("C:\python-level-two\music\Greatman_Takit_-_Correct_CeeNaija.com_.mp3")
pygame.mixer.music.play()
time.sleep(20)
pygame.mixer.music.stop()