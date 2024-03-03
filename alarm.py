# # import pygame
# # import datetime as dt
import time
import re


# # file = (r"C:\python-level-two\music\Greatman_Takit_-_Correct_CeeNaija.com_.mp3")

# # while True:
# #     tm = dt.datetime.now()
# #     if tm.strftime('%I') == "08" and tm.strftime("%M") == "52" and tm.strftime("%S") == "00" and tm.strftime("%p") == "AM":
# #         print("Its time to play.")
# #         pygame.init()
# #         pygame.mixer.music.load(file)
# #         pygame.mixer.music.play()
# #         time.sleep(20)
# #         pygame.mixer.music.stop()

# # email = input('Email: '.strip())
# # pattern = r'\w+@\w+\.\w+'
# # username = re.findall(pattern, email)
# # if username:
# #     print(f"Your username is {'username'}")
# # else:
# #     print('error')

# ===============================

# words = 'Solomon is a great man of God.'
# word = words.split() 
# print(word)
# wordjoin = '^'.join(word)
# print(wordjoin)

# key = input(': ').strip().title()
# # print(key)


# class MAN:
    
    
    # ============ palindrome ===============
# user = input('Enter word to test: ')
# user.split
# word = ''.join(users)

#     # test for palindrome
    
# if word != word[::-1]:
#     print('Word not a palindrome')
# else:
#     print('Word is a palindrome')



# pattern = r'\w+\d+@gmail.com'
# e_mail = input("Please enter your mail: ")
# if pattern == e_mail:
#     print('Correct')
# else:
#     print('Error')

# age = int(input('Your Age: '))
# if age < 18:
#     print('You are not of legal age')
#     time.sleep(2)
#     print('Go home')
#     exit()
# else:
#     print('Legal age')
#     print('Proceed to start')


# ================== ussd ===============

# def ussd():
#     ussd = input('Enter USSD: ')
#     while ussd != '*312#':
#         print("Invalid USSD CODE. TRY *312# ")
#         ussd = input('Enter USSD: ')

#     print("""
        
#         Welcome

#         1. buy data
#         2. transfer
        
#         """)
   

    

# ussd()

# =====================================

pattern = r'\w+\d+@\w+\.\w+'
e_mail = input("Please enter your mail: ")
match = re.match(pattern,e_mail)
if not match:
    print('Email Mismatch.. TRY "ask11@gmail.com"')
else:
    print('Perfect match')