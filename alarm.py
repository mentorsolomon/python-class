# # import pygame
# # import datetime as dt
import time
import random
import re

# from inherintance import PARENT

# import inherintance



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

# pattern = r'\w+\d+@\w+\.\w+'
# e_mail = input("Please enter your mail: ")
# match = re.match(pattern,e_mail)
# if not match:
#     print('Email Mismatch.. TRY "ask11@gmail.com"')
# else:
#     print('Perfect match')



# wake =  input('phone number: ').strip('0'.startswith('0'))
# print(wake)

# =================================

        
#    =================================================

# x = 10
# while x > 0:
#     print(f'Leave the class {x}')
#     x -= 1
# else:
#     print('Condition successful')
# =========================================================
# x = 1
# while x <= 10:
#     print(f'You are welcome to class {x}')
#     x += 1
# # print(x)

      
# while pin != user:
#     print('Wrong, try again')
#     x = x-1
# else:
#     print('Welcome')
#     break

# while loop approach ================================

# pin = '2222'
# user = input('Enter Pin: ').strip()
# x = 4

# while x > 0:
#     if user == pin:
#         print('Welcome')
#         break
#     else:
#         print(f'You have {x} attempt(s) left.\n')
#         user = input('Enter Pin: ').strip()
#         x -= 1
#         if x == 2:
#             if user !=pin:
#                 print('Account will be Logged out automatically on the final attempt if wrong.')
#         if x == 1:
#             if user != pin:
#                 time.sleep(2)
#                 print('Account Logged Out.')
#                 exit()   


# ========== FOR loop approach =====================
# for num in range(1,4):
#     user = input('Enter your pin: ').strip()
#     if user == pin:
#         time.sleep(2)
#         print("welcome")
#         break
#     else:
#         if num == 1:
#             if user != pin:
#                 print('You have 2 attempts left')
#         elif num == 2:
#             if user != pin:
#                 print('You have 1 attempt left. ')
#                 time.sleep(2)
#                 print('Account will be automatically logged out on final attempt.')
#                 time.sleep(3)
#         elif num == 3:
#             if user != pin:
#                 print('Account Logged out.')
#                 time.sleep(2)
#                 exit()

# =====================
def game():
    # try:
    #     earn = 0
    #     x = random.randint(1, 15)
    #     user = int(input('Guess the number: '))
    #     print(f'\n{x} is the correct number')
    #     if user == x:
    #         print('Guess right')
    #         earn+=10
    #         print(f'You have won #{earn}')
    #         game()
    #     else:
    #         print('\nWrong answer. Try again')
    #         game()
    # except ValueError:
    #     print('Integer expected.')
    #     game()



    # pattern = (r'\d+\w+@\w+\.\w+') or (r'\w+\d+@\w+\.\w+') 
    # ee_mail = input('Email >> ').strip()
    # match = re.search(pattern,ee_mail)
    # if not match:
    #     print('Email Mismatch.. TRY "ask11@gmail.com"')
    #     # self.mail_checker()
    # else:
    #     print('Pattern Found')
# ==============================================================
    balance = []

    # amount = 5

    # balance+=amount*5
    # print('#',{amount*5},"added to Balance")
    # print((balance))

    game_sets = []
    for nums in range(1,41):
        game_sets.append(nums)
        print(game_sets)
    print(game_sets)
    


            


game()
