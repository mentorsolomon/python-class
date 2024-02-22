# import pygame
# import datetime as dt
# import time
import re


# file = (r"C:\python-level-two\music\Greatman_Takit_-_Correct_CeeNaija.com_.mp3")

# while True:
#     tm = dt.datetime.now()
#     if tm.strftime('%I') == "08" and tm.strftime("%M") == "52" and tm.strftime("%S") == "00" and tm.strftime("%p") == "AM":
#         print("Its time to play.")
#         pygame.init()
#         pygame.mixer.music.load(file)
#         pygame.mixer.music.play()
#         time.sleep(20)
#         pygame.mixer.music.stop()

email = input('Email: '.strip())
username = email.strip('@\w+\.\w+')
print(f"Your username is {username}")
