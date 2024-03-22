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
# user = ''.join(user)

#     # test for palindrome
    
# if user != user[::-1]:
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
# def game():
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
    # balance = []

    # amount = 5

    # balance+=amount*5
    # print('#',{amount*5},"added to Balance")
    # print((balance))

    # game_sets = []
    # for nums in range(1,41):
    #     game_sets.append(nums)
    #     print(game_sets)
    # print('\n')
    # print(game_sets)
    # print('\n')

    # numbers_list = []
    # for numbers in range(1,101):
    #     numbers_list.append(numbers)
    # print(numbers_list)    


    # =================================
    # score = 0
    # exam = {
    #     "1. What is the capital of Ghana a.) Accra b.) Utanbatoor": "a",
    #     "2. What is the capital of Nigeria a.) Abuja b.) Rivers": "a",
    #     "3. What is the capital of Tunisia a.) Jebba b.) Leona": "b",
    #     "4. What is the capital of Togo a.) Lome b.) Gertha": "a",
    #     "5. What is the capital of Germany a.) Munchen b.) Berlin": "b",
    #     "6. What is the capital of Sweden a.) Heilsinki b.) Stockholm": "b",
    #     "7. What is the capital of Cape Verde a.) Praia b.) Ladta": "a",
    #     "8. What is the capital of South Africa a.) Cape Town b.) Johannesburg": "a",
    #     "9. What is the capital of Oyo a.) Ibadan b.) Oyo": "a",
    #     "10. What is the capital of Lagos a.) Ikeja b.) Alimosho": "a",
    # }

    # for question, answers in exam.items():
    #     print(question)
    #     user = input('answer: ').strip().lower()
    #     if user != answers:
    #         print('wrong')
    #     else:
    #         print('correct')
    #         score += 10
    # print(score)

    # solo = [1,2,3,4,5,6,1]
    # # print(solo.index(1))
    # xy = 1
    # y = 0
    # ===========================================

    # word = input('PALINDROME CHECKER: ').strip().lower()
    # word_split = word.split()
    # word_join = "".join(word_split)
    # print(word_join, word_split)
    # if word_join != word_join[::-1]:
    #     print('Not a palindrome')
    # else:
    #     print('PAlindrome')









    # ===========================================
    # for x in solo:
    #     if x == xy:
    # #         print(solo.index(xy)) 
    # #         y+=1 
    # # print('DONE')

    # weight = input('Enter weight in kg or lbs: ').strip().lower()
    # print(weight)

    # print('\n')

    # if weight.endswith('kg'):
    #     x = int(weight.strip('kg'))
    #     weight_in_pounds = x/0.453
    #     print(f'Your weight in pounds is {weight_in_pounds}lbs.')
    # elif weight.endswith('lbs'):
    #     x = int(weight.strip('lbs'))
    #     weight_in_kg = (x*0.453)
    #     weight_in_kg = round(weight_in_kg, 2)
    #     print(f'Your weight in kilogram is {weight_in_kg}Kg.')
    # else:
    #     print('Enter A COMMAND ENDING IN KG OR LBS')       

# 
# game()


# =======================================
# sett = set(range(1, 7))
# # print(sett)
# for sets in sett:
#     print(sets)
    # if sets == 1:
    #     set_items = int(input(f'How many data items are in your set{set+1} > ').strip())
    #     for entries in range(set_items):
    #         entry = int(input(f'Your data item {entries + 1} is > ').strip())
    #         sett.update(entry)
    #         print(sett)

# ========================================
# SET CALCULATOR

from time import sleep

print('''
    WELCOME TO SET CALCULATOR.

...Kindly provide the following informationn...    
    ''')   
list_sets = []

try:
    sets_in_list = int(input('How many sets do you have: ').strip())

    for num in range(sets_in_list):
        set_items = int(input(f'How many items are in Set{num+1}>> ').strip())
        items = []
        count = 1

        for data_items in range(set_items):
            item = int(input(f'Item{data_items+1}: ').strip())
            items.append(item)
            count+=1

        list_sets.append(set(items))
        sleep(2)

        
    var = 1

    for sets in list_sets:
        print(f"""
        Set{var} = {sets}
        """)
        var+=1



    sleep(3)
    user = input(f'''
        Note, you can only compare two sets, irrespective of how many you have provided.
        
        What operation will you like to perform
        1. Union
        2. Intersection
        3. Difference
        4. Symmetric_difference
        5. exit
    >>>> 

    ''').strip()

    sleep(2)
    if user == '1':
        print(f'''
        You have {len(list_sets)} saved Sets
        Kindly select
        ''')
        setA = set(list_sets[(int(input('What is your setA: ').strip())) - 1])
        setB = set(list_sets[(int(input('What is your setB: ').strip())) - 1])
        sleep(3)
        print(f'{setA} union {setB} = {setA.union(setB)}')
    
        

    elif user == '2':
        print(f'''
        You have {len(list_sets)} saved Sets
        Kindly select...
        ''')
        setA = set(list_sets[(int(input('What is your setA: ').strip())) - 1])
        setB = set(list_sets[(int(input('What is your setB: ').strip())) - 1])
        sleep(3)
        print(f'{setA} intersection {setB} = {setA.intersection(setB)}')
    


    elif user == '3':
        print(f'''
        You have {len(list_sets)} saved Sets
        Kindly select with priority to the one you want to perform the operation on.
        ''')
        setA = set(list_sets[(int(input('What is your setA: ').strip())) - 1])
        setB = set(list_sets[(int(input('What is your setB: ').strip())) - 1])
        sleep(3)
        print(f'{setA} difference {setB} = {setA.difference(setB)}')
        sleep(2)
    

    elif user == '4':
        print(f'''
        You have {len(list_sets)} saved Sets
        Kindly select...
        ''')
        setA = set(list_sets[(int(input('What is your setA: ').strip())) - 1])
        setB = set(list_sets[(int(input('What is your setB: ').strip())) - 1])
        sleep(3)
        print(f'{setA} symmetric_difference {setB} = {setA.symmetric_difference(setB)}')
        sleep(2)
        


    elif user =='5':
        sleep(2)
        exit()


    else:
        print('Invalid Command. Try again from the top.')
        sleep(2)
        

except Exception as e:
    print(f'{e}. Try again')



   
        